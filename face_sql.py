import pandas as pd
import mysql.connector


# Connect to SQL Server
conn = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                              database='social listening',
                              use_pure=False)

print(conn)
cursor = conn.cursor()

# STATUS
data_status = pd.read_csv (r'status.csv')   
status = pd.DataFrame(data_status)


# Create Table Status
cursor.execute('''
		CREATE TABLE Status (
            ID INTEGER NOT NULL PRIMARY KEY  AUTO_INCREMENT
            ,All_Status        INTEGER  NOT NULL 
            ,Like_Status       INTEGER  NOT NULL
            ,Love_Status       INTEGER  NOT NULL
            ,Care_Status       INTEGER  NOT NULL
            ,Haha_Status       INTEGER  NOT NULL
            ,Sad_Status        INTEGER  NOT NULL
            ,Angry_Status      INTEGER  NOT NULL
            ,Wow_Status        INTEGER  NOT NULL
            );
            ''')

# Insert DataFrame to Table Replys_Status
for reply_s in data_status.itertuples():
    cursor.execute('''
                INSERT INTO Status (All_Status, Like_Status, Love_Status, Care_Status, 
                Haha_Status, Sad_Status, Angry_Status, Wow_Status) 
                VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")
                ''',
                (reply_s.All, 
                reply_s.Like,
                reply_s.Love,
                reply_s.Care,
                reply_s.Haha, 
                reply_s.Sad, 
                reply_s.Angry, 
                reply_s.Wow)
                )


# POSTS
data_posts = pd.read_csv (r'posts.csv')   
posts = pd.DataFrame(data_posts)

# # Create Table Posts
cursor.execute('''
            CREATE TABLE Posts(
                ID INTEGER NOT NULL PRIMARY KEY  AUTO_INCREMENT
                ,ID_Post        INTEGER  NOT NULL  
                ,Content         VARCHAR(1726) NOT NULL
                ,Post_date       VARCHAR(16)
                ,Sentiment       VARCHAR(30)
                ,Share           INTEGER  NOT NULL
                ,Source_division INTEGER  NOT NULL
                ,Title           VARCHAR(129)
                ,Total_comment   INTEGER  NOT NULL
                ,Url             VARCHAR(275) NOT NULL
                ,Username        VARCHAR(17) NOT NULL
                ,ID_Status           INTEGER  NOT NULL
                ,FOREIGN KEY (ID_Status) REFERENCES Status(ID)
                );
               ''')


# Insert DataFrame to Table Posts
for post in data_posts.itertuples():
    cursor.execute('''INSERT INTO Posts (ID_Post, Content, Post_date, Sentiment, Share, \
                   Source_division, Title, Total_comment, Url, Username, ID_Status) \
                   VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")''',
                (post.id_post, 
                post.content,
                post.post_date,
                post.sentiment,
                post.share,
                post.source_division,
                post.title,
                post.total_comment,
                post.url,
                post.username,
                post.id_status)
                )


# COMMENTS
data_comments = pd.read_csv (r'comments.csv')   
comments = pd.DataFrame(data_comments)

# Create Table Comments
cursor.execute('''
		CREATE TABLE Comments(
            ID INTEGER NOT NULL PRIMARY KEY  AUTO_INCREMENT
            ,ID_Comment       INTEGER  NOT NULL 
            ,ID_Post   INTEGER  NOT NULL
            ,Post_date VARCHAR(16)
            ,Sentiment VARCHAR(30)
            ,Content   VARCHAR(307) NOT NULL
            ,FOREIGN KEY (ID_Post) REFERENCES Posts(ID)
            ,ID_Status           INTEGER  NOT NULL
            ,FOREIGN KEY (ID_Status) REFERENCES Status(ID)
            );
               ''')

# Insert DataFrame to Table Comments
for comment in data_comments.itertuples():
    cursor.execute('''
                INSERT INTO Comments (ID_Comment, ID_Post, Post_date, Sentiment, Content, ID_Status)
                VALUES ("%s", "%s", "%s", "%s", "%s", "%s")
                ''',
                (comment.id_comment, 
                comment.id_post,
                comment.post_date,
                comment.sentiment,
                comment.content,
                comment.id_status)
                )


# REPLYS
data_replys = pd.read_csv (r'replys.csv')   
replys = pd.DataFrame(data_replys)

# Create Table Replys
cursor.execute('''
		CREATE TABLE Replys(
            ID INTEGER NOT NULL PRIMARY KEY  AUTO_INCREMENT
            ,ID_Reply       INTEGER  NOT NULL 
            ,ID_Comment   INTEGER  NOT NULL
            ,Post_date VARCHAR(16)
            ,Sentiment VARCHAR(30)
            ,Content   VARCHAR(307) NOT NULL
            ,FOREIGN KEY (ID_Comment) REFERENCES Comments(ID)
            ,ID_Status           INTEGER  NOT NULL
            ,FOREIGN KEY (ID_Status) REFERENCES Status(ID)
            );
               ''')

# Insert DataFrame to Table Replys
for reply in data_replys.itertuples():
    cursor.execute('''
                INSERT INTO Replys (ID_Reply, ID_Comment, Post_date, Sentiment, Content, ID_Status)
                VALUES ("%s", "%s", "%s", "%s", "%s", "%s")
                ''',
                (reply.id_reply, 
                reply.id_comment,
                reply.post_date,
                reply.sentiment,
                reply.content,
                reply.id_status)
                )

conn.commit()