import json
import csv
import codecs


def save_csv(path):
    with open(path, 'r', encoding='utf-8') as f:
        posts = json.load(f)

    list_post = []
    list_comment = []
    list_status_post = []
    list_status_comment = []
    list_reply = []

    for post in posts:
        # POST
        list_post.append([
            int(post['id_post']),
            post['content'],
            post['post_date'],
            post['setiment'],
            int(post['share']),
            int(post['source_division']),
            post['title'],
            int(post['total comment']),
            post['url'],
            post['username']
        ])
        # POST STATUS
        status_dict_post = post['status_dict'].values()
        # status_dict_post.append(int(post['id_post']))
        list_status_post.append(status_dict_post)

        # COMMENT
        comments = post['comments']
        for comment in comments:
            list_comment.append([int(comment['id_comment']),
                                int(comment['id_post']),
                                comment['post_date'],
                                comment['setiment'],
                                comment['content']])
            # COMMENT STATUS
            status_dict_comment = comment['status_dict'].values()
            # status_dict_comment.append(comment['id_comment'])
            list_status_comment.append(status_dict_comment)

            # REPLY
            replys = comment['replys']
            for reply in replys:
                list_reply.append([int(reply['id_reply']),
                                    int(reply['id_comment']),
                                    reply['post_date'],
                                    reply['setiment'],
                                    reply['content']])
                # REPLY STATUS
                status_dict_reply = reply['status_dict'].values()
                # status_dict_reply.append(reply['id_reply'])
                list_status_comment.append(status_dict_reply)


    # SAVE POSTS
    posts = codecs.open('posts.csv', 'w', 'utf-8')
    with posts:
        writer = csv.writer(posts)
        writer.writerows(list_post)

    # SAVE COMMENT
    comments = codecs.open('comments.csv', 'w', 'utf-8')
    with comments:
        writer = csv.writer(comments)
        writer.writerows(list_comment)

    # SAVE POST_STATUS
    post_status = codecs.open('post_status.csv', 'w', 'utf-8')
    with post_status:
        writer = csv.writer(post_status)
        writer.writerows(list_status_post)

    # SAVE COMMENT_STATUS
    comment_status = codecs.open('comment_status.csv', 'w', 'utf-8')
    with comment_status:
        writer = csv.writer(comment_status)
        writer.writerows(list_status_comment)

    # SAVE REPLYS
    replys = codecs.open('replys.csv', 'w', 'utf-8')
    with replys:
        writer = csv.writer(replys)
        writer.writerows(list_reply)


save_csv("face1.json")