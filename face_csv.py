import json
import csv
import codecs


def save_csv(path):
    with open(path, 'r', encoding='utf-8') as f:
        posts = json.load(f)

    list_post = [["id_post", "content", "post_date", "sentiment", 
                        "share", "source_division", "title", "total_comment",
                            "url", "username", "id_status"]]
    list_comment = [["id_comment", "id_post", "post_date", "sentiment", "content", "id_status"]]
    list_reply = [["id_reply", "id_comment", "post_date", "sentiment", "content", "id_status"]]
    list_status = [["All", "Like", "Love", "Care", "Haha", "Sad", "Angry", "Wow"]]
    

    idx = 1
    for post in posts:
        # POST
        list_post.append([
            post['id_post'],
            post['content'],
            post['post_date'],
            post['sentiment'],
            int(post['share']),
            int(post['source_division']),
            post['title'],
            int(post['total comment']),
            post['url'],
            post['username'],
            idx
        ])
        # POST STATUS
        status_dict_post = list(post['status_dict'].values())
        idx += 1
        list_status.append(status_dict_post)

        # COMMENT
        comments = post['comments']
        for comment in comments:
            list_comment.append([int(comment['id_comment']),
                                int(comment['id_post']),
                                comment['post_date'],
                                comment['sentiment'],
                                comment['content'],
                                idx]
                                )
            # COMMENT STATUS
            status_dict_comment = list(comment['status_dict'].values())
            idx += 1
            list_status.append(status_dict_comment)

            # REPLY
            replys = comment['replys']
            for reply in replys:
                list_reply.append([int(reply['id_reply']),
                                    int(reply['id_comment']),
                                    reply['post_date'],
                                    reply['sentiment'],
                                    reply['content'],
                                    idx]
                                    )
                # REPLY STATUS
                status_dict_reply = list(reply['status_dict'].values())
                idx += 1
                list_status.append(status_dict_reply)


    # SAVE POSTS
    posts = codecs.open('./posts.csv', 'w', 'utf-8')
    with posts:
        writer = csv.writer(posts)
        writer.writerows(list_post)


    # SAVE COMMENT
    comments = codecs.open('./comments.csv', 'w', 'utf-8')
    with comments:
        writer = csv.writer(comments)
        writer.writerows(list_comment)


    # SAVE REPLYS
    replys = codecs.open('./replys.csv', 'w', 'utf-8')
    with replys:
        writer = csv.writer(replys)
        writer.writerows(list_reply)


    # SAVE POST_STATUS
    status = codecs.open('./status.csv', 'w', 'utf-8')
    with status:
        writer = csv.writer(status)
        writer.writerows(list_status)


save_csv("face.json")