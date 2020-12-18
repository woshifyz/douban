import requests
import json

data = '{"data": [{"type": "hot_list_feed", "style_type": "1", "id": "0_1607863181.8270018", "card_id": "Q_434611425", "target": {"id": 434611425, "title": "2020 \u5e74\u5feb\u7ed3\u675f\u4e86\uff0c\u79cb\u51ac\u5404\u5730\u9646\u7eed\u51fa\u73b0\u6563\u53d1\u75c5\u4f8b\uff0c\u75ab\u60c5\u53d1\u5c55\u4f1a\u5f71\u54cd\u6625\u8282\u56de\u5bb6\u8fc7\u5e74\u5417\uff1f", "url": "https://api.zhihu.com/questions/434611425", "type": "question", "created": 1607829118, "answer_count": 81, "follower_count": 585, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [1400, 4080, 5582, 566991, 666595], "comment_count": 1, "is_following": false, "excerpt": "\u6700\u65b0\u6d88\u606f \u636e\u9ed1\u9f99\u6c5f\u7701\u536b\u5065\u59d4\u7f51\u7ad9\u6d88\u606f\uff0c2020\u5e7412\u670812\u65e50-24\u65f6\uff0c\u9ed1\u9f99\u6c5f\u7701\u65b0\u589e\u65b0\u51a0\u80ba\u708e\u786e\u8bca\u75c5\u4f8b5\u4f8b(\u7ee5\u82ac\u6cb3\u5e02\u672c\u571f3\u4f8b\u3001\u4e1c\u5b81\u5e02\u672c\u571f1\u4f8b\u3001\u5854\u6cb3\u53bf\u5883\u5916\u8f93\u5165\u65e0\u75c7\u72b6\u611f\u67d3\u8005\u8f6c\u4e3a\u786e\u8bca\u75c5\u4f8b1\u4f8b)\uff0c\u65e0\u65b0\u589e\u65e0\u75c7\u72b6\u611f\u67d3\u8005\u3002 \u622a\u81f32020\u5e7412\u670812\u65e524\u65f6\uff0c\u73b0\u6709\u786e\u8bca\u75c5\u4f8b7\u4f8b(\u4e1c\u5b81\u5e02\u672c\u571f2\u4f8b\u3001\u7ee5\u82ac\u6cb3\u5e02\u672c\u571f4\u4f8b\u3001\u5854\u6cb3\u53bf\u5883\u5916\u8f93\u51651\u4f8b)\uff0c\u73b0\u6709\u65e0\u75c7\u72b6\u611f\u67d3\u80052\u4f8b(\u7ee5\u82ac\u6cb3\u5e02\u672c\u571f2\u4f8b)\u3002 \u65b0\u589e\u786e\u8bca\u75c5\u4f8b\u60c5\u51b5\uff1a \u75c5\u4f8b1\uff1a\u5973\uff0c33\u5c81\uff0c\u65e0\u4e1a\uff0c\u73b0\u4f4f\u7ee5\u82ac\u6cb3\u5e02\u6d77\u878d\u5bcc\u534e\u82d1\u3002 \u75c5\u4f8b2\uff1a\u7537\uff0c6\u5c81\uff0c\u7ee5\u82ac\u6cb3\u5e02\u67d0\u5c0f\u5b66\u5b66\u751f\u3002 \u75c5\u4f8b3\uff1a\u7537\uff0c4\u5c81\uff0c\u7ee5\u82ac\u6cb3\u5e02\u67d0\u5e7c\u513f\u56ed\u513f\u7ae5\u3002"}, "attached_info": "CkcIo9aVgv6XqKVuEAMaCDU4ODU5MzEzIP6M1v4FMAE4yQRAAHIJNDM0NjExNDI1eACqARFiaWxsYm9hcmQtc2NpZW5jZdIBAA==", "detail_text": "346 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": false, "children": [{"type": "answer", "thumbnail": "https://pic4.zhimg.com/50/v2-9f0383493362a7991e5529357ff79916_b.jpg"}]}, {"type": "hot_list_feed", "style_type": "1", "id": "1_1607863181.8277895", "card_id": "Q_341125873", "target": {"id": 341125873, "title": "\u6211\u4eec\u6bcf\u5929\u81ea\u5f8b\u3001\u8ba4\u771f\u5b66\u4e60\u6700\u7ec8\u7684\u76ee\u7684\u5230\u5e95\u662f\u4ec0\u4e48\uff1f", "url": "https://api.zhihu.com/questions/341125873", "type": "question", "created": 1566051138, "answer_count": 4056, "follower_count": 17783, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [5361, 10110, 13352, 17419, 41299], "comment_count": 44, "is_following": false, "excerpt": ""}, "attached_info": "CkgIo9aVgv6XqKVuEAMaCDM4MDgyNzI5IMKW4OoFMCw494oBQAFyCTM0MTEyNTg3M3gAqgERYmlsbGJvYXJkLXNjaWVuY2XSAQA=", "detail_text": "314 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": false, "children": [{"type": "answer", "thumbnail": "https://pic3.zhimg.com/80/v2-00d32c960139399d222eff2804441d53_hd.jpg"}]}, {"type": "hot_list_feed", "style_type": "1", "id": "2_1607863181.8282647", "card_id": "Q_434492097", "target": {"id": 434492097, "title": "\u65b0\u7586\u5410\u9c81\u756a\u65b0\u589e 3 \u4f8b\u672c\u571f\u65e0\u75c7\u72b6\u611f\u67d3\u8005\uff0c\u76ee\u524d\u60c5\u51b5\u600e\u4e48\u6837\uff1f", "url": "https://api.zhihu.com/questions/434492097", "type": "question", "created": 1607753163, "answer_count": 34, "follower_count": 139, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [12133, 389272, 566991, 567779, 583976], "comment_count": 1, "is_following": false, "excerpt": "\u5410\u9c81\u756a\u5e02\u536b\u751f\u5065\u5eb7\u59d4\u6700\u65b0\u901a\u62a5\uff0c12\u670812\u65e5\uff0c\u5410\u9c81\u756a\u5e02\u9ad8\u660c\u533a\u5728\u5bf9\u91cd\u70b9\u4eba\u7fa4\u8fdb\u884c\u5b9a\u671f\u6838\u9178\u68c0\u6d4b\u4e2d\uff0c\u53d1\u73b01\u540d\u9633\u6027\u4eba\u5458\uff0c\u7ecf\u4e13\u5bb6\u8bca\u65ad\u4e3a\u65e0\u75c7\u72b6\u611f\u67d3\u8005\u3002 \u9996\u4f8b\u65e0\u75c7\u72b6\u611f\u67d3\u8005\uff0c\u7537\uff0c32\u5c81\uff0c\u4e3a\u5410\u9c81\u756a\u5e02\u7ecf\u5f00\u533a\u4e00\u5546\u8d38\u516c\u53f8\u5458\u5de5\uff0c\u5bb6\u4f4f\u5410\u9c81\u756a\u5e02\u9ad8\u660c\u533a\u7ea2\u76fe\u5c0f\u533a\u3002 \u53d1\u73b0\u9996\u4f8b\u65e0\u75c7\u72b6\u611f\u67d3\u8005\u540e\uff0c\u5410\u9c81\u756a\u5e02\u75be\u63a7\u90e8\u95e8\u8fc5\u901f\u6392\u67e5\u5176\u5bc6\u5207\u63a5\u89e6\u8005\u53ca\u5bc6\u5207\u63a5\u89e6\u8005\u7684\u5bc6\u5207\u63a5\u89e6\u8005\uff0c\u5168\u90e8\u8fdb\u884c\u6838\u9178\u68c0\u6d4b\u3002\u8be5\u65e0\u75c7\u72b6\u611f\u67d3\u8005\u7684\u59bb\u5b50(28\u5c81)\u3001\u6bcd\u4eb2(63\u5c81)\u6838\u9178\u68c0\u6d4b\u7ed3\u679c\u5448\u9633\u6027\uff0c\u5176\u4f59\u4eba\u5458\u5747\u4e3a\u9634\u6027\u3002\u76ee\u524d\uff0c3\u4f8b\u65e0\u75c7\u72b6\u611f\u67d3\u8005\u5747\u5df2\u9001\u81f3\u5b9a\u70b9\u533b\u9662\u8fdb\u884c\u9694\u79bb\u533b\u5b66\u89c2\u5bdf\u3002"}, "attached_info": "CkcIo9aVgv6XqKVuEAMaCDU4ODMyNzc2IMu70f4FMAE4iwFAAnIJNDM0NDkyMDk3eACqARFiaWxsYm9hcmQtc2NpZW5jZdIBAA==", "detail_text": "188 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": false, "children": [{"type": "answer", "thumbnail": "https://pic1.zhimg.com/80/v2-f6f5d1ee7772b2feb4c0c8d65dd2a391_720w.jpg?source=1940ef5c"}]}, {"type": "hot_list_feed", "style_type": "1", "id": "3_1607863181.82886", "card_id": "Q_426002620", "target": {"id": 426002620, "title": "\u591a\u559d\u5976\u5bf9\u957f\u9ad8\u6709\u7528\u5417?", "url": "https://api.zhihu.com/questions/426002620", "type": "question", "created": 1602866002, "answer_count": 230, "follower_count": 875, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [11076, 14845, 170534], "comment_count": 6, "is_following": false, "excerpt": "\u6211\u9ad8\u4e8c\uff0c\u73b0\u5728\u6bcf\u5929\u4e24\u74f6\u5976\uff0c\u4f46\u662f\u611f\u89c9\u5f88\u957f\u65f6\u95f4\u6ca1\u957f\u4e2a\u4e86\uff0c\u5982\u679c\u6211\u4e00\u5929\u559d\u56db\u74f6\uff0c\u4f1a\u5bf9\u6211\u957f\u9ad8\u6709\u597d\u5904\u5417\uff1f"}, "attached_info": "CkcIo9aVgv6XqKVuEAMaCDU2OTQ2NTEzINKWp/wFMAY46wZAA3IJNDI2MDAyNjIweACqARFiaWxsYm9hcmQtc2NpZW5jZdIBAA==", "detail_text": "182 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": false, "children": [{"type": "answer", "thumbnail": "https://pic4.zhimg.com/v2-f60b828d30903eec2eb7ee5895528992_1440w.jpg?source=172ae18b"}]}, {"type": "hot_list_feed", "style_type": "1", "id": "4_1607863181.8292882", "card_id": "Q_434496090", "target": {"id": 434496090, "title": "\u5982\u4f55\u770b\u5f85\u5c71\u897f\u8fd0\u57ce\u9a6c\u620f\u56e2\u8001\u864e\u5931\u63a7\u54ac\u4eba\uff0c\u9a6c\u620f\u56e2\u662f\u5426\u5e94\u8be5\u88ab\u53d6\u7f14\uff1f", "url": "https://api.zhihu.com/questions/434496090", "type": "question", "created": 1607755122, "answer_count": 52, "follower_count": 194, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [444, 1027, 1571, 4890, 25450], "comment_count": 0, "is_following": false, "excerpt": "\u8b66\u65b9\uff1a\u8001\u864e\u6ca1\u6709\u7259\u4ec5\u8f7b\u5fae\u4f24\u300212\u670811\u65e5\uff0c\u5c71\u897f\u8fd0\u57ce\u3002\u4e00\u5bb6\u5ead\u7ecf\u8425\u7684\u9a6c\u620f\u56e2\u6f14\u51fa\u65f6\uff0c\u4e00\u53ea\u8868\u6f14\u8001\u864e\u7a81\u7136\u6251\u5411\u9a6f\u517d\u5e08\u6495\u54ac\u3002\u5176\u4ed6\u4eba\u5458\u8fde\u5fd9\u4e0a\u524d\u963b\u6b62\uff0c\u89c2\u4f17\u4e00\u7247\u60ca\u547c\u3002\u636e\u4e86\u89e3\uff0c\u73b0\u573a\u6709\u4e24\u540d\u9a6f\u517d\u5e08\u53d7\u4f24\u9001\u533b\u3002\u8f96\u533a\u8b66\u65b9\u56de\u5e94\u8001\u864e\u6ca1\u6709\u7259\uff0c\u88ab\u54ac\u7684\u662f\u9a6f\u517d\u5e08\u4ec5\u8f7b\u5fae\u4f24\u3002\u6574\u4e2a\u8fc7\u7a0b\u90fd\u5728\u7b3c\u5b50\u91cc\uff0c\u7b3c\u5916\u56f4\u89c2\u7fa4\u4f17\u65e0\u4eba\u53d7\u4f24\u3002"}, "attached_info": "CkcIo9aVgv6XqKVuEAMaCDU4ODMzNjQ1IPLK0f4FMAA4wgFABHIJNDM0NDk2MDkweACqARFiaWxsYm9hcmQtc2NpZW5jZdIBAA==", "detail_text": "167 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": false, "children": [{"type": "answer", "thumbnail": "https://pic1.zhimg.com/50/v2-7f66a108b88980c02a46577187ca732c_b.jpg"}]}, {"type": "hot_list_feed", "style_type": "1", "id": "5_1607863181.8297367", "card_id": "Q_434517976", "target": {"id": 434517976, "title": "\u5982\u4f55\u770b\u5f85\u6c88\u9633\u89c4\u5b9a\u7535\u68af\u7ef4\u62a4\u4eba\u5458\u987b\u5728\u63a5\u5230\u56f0\u4eba\u62a5\u544a\u540e 30 \u5206\u949f\u5185\u62b5\u8fbe\u73b0\u573a\u6551\u63f4\uff0c\u8fdd\u89c4\u6700\u9ad8\u7f5a 10 \u4e07\uff1f", "url": "https://api.zhihu.com/questions/434517976", "type": "question", "created": 1607765533, "answer_count": 19, "follower_count": 40, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [215, 3423, 5582, 20070, 26317], "comment_count": 0, "is_following": false, "excerpt": "\u300a\u6c88\u9633\u5e02\u7535\u68af\u5b89\u5168\u6761\u4f8b\u300b\u5c06\u4e8e2021\u5e741\u67081\u65e5\u8d77\u6b63\u5f0f\u65bd\u884c\u3002 \u4e3a\u4e86\u907f\u514d\u51fa\u73b0\u201c\u6020\u4e8e\u6551\u63f4\u201d\u95ee\u9898\uff0c\u300a\u6761\u4f8b\u300b\u89c4\u5b9a\uff0c\u7535\u68af\u7ef4\u62a4\u4fdd\u517b\u5355\u4f4d\u5e94\u5f53\u5236\u5b9a\u5e94\u6025\u63aa\u65bd\u548c\u6551\u63f4\u9884\u6848\uff0c\u5e94\u6025\u6551\u63f4\u7535\u8bdd\u5e94\u5f53\u4fdd\u630124\u5c0f\u65f6\u6709\u6548\u5e94\u7b54\u3002 \u63a5\u5230\u7535\u68af\u56f0\u4eba\u62a5\u544a\u540e\uff0c\u7535\u68af\u7ef4\u62a4\u4fdd\u517b\u4eba\u5458\u5e94\u5f53\u572830\u5206\u949f\u5185\u62b5\u8fbe\u6240\u7ef4\u62a4\u4fdd\u517b\u7535\u68af\u6240\u5728\u5730\u5b9e\u65bd\u73b0\u573a\u6551\u63f4\u3002\u8fdd\u53cd\u4ee5\u4e0a\u89c4\u5b9a\u7684\uff0c\u7535\u68af\u7ef4\u62a4\u4fdd\u517b\u5355\u4f4d\u5c06\u88ab\u5904\u4ee51\u4e07\u5143\u4ee5\u4e0a10\u4e07\u5143\u4ee5\u4e0b\u7f5a\u6b3e\u3002 \u5bf9\u4e8e\u65b0\u5b89\u88c5\u8f7d\u4eba\u7535\u68af\u7684\uff0c\u300a\u6761\u4f8b\u300b\u4f5c\u51fa\u4e86\u89c4\u5b9a\uff0c\u8981\u6c42\u65b0\u7535\u68af\u5e94\u5f53\u5b89\u88c5\u5177\u5907\u8fd0\u884c\u53c2\u6570\u91c7\u96c6\u3001\u4fe1\u606f\u7f51\u7edc\u4f20\u8f93\u3001\u81ea\u52a8\u62a5\u8b66\u3001\u5b9e\u65f6\u901a\u8bdd\u7b49\u529f\u80fd\u7684\u7269\u8054\u7f51\u7535\u68af\u7cfb\u7edf\uff0c\u6309\u7167\u89c4\u5b9a\u914d\u5907\u7edf\u4e00\u63a5\u53e3\uff0c\u5e76\u5bf9\u5e02\u6216\u8005\u533a\u3001\u53bf\uff08\u5e02\uff09\u5e02\u573a\u76d1\u7763\u7ba1\u7406\u90e8\u95e8\u5f00\u653e\u3002 \u300a\u6761\u4f8b\u300b\u8981\u6c42\uff0c\u516c\u4f17\u805a\u96c6\u573a\u6240\u548c\u4f4f\u5b85\u5b89\u88c5\u7535\u68af\u7684\uff0c\u5e94\u8bbe\u7f6e\u53cc\u7535\u6e90\u3001\u53cc\u56de\u8def\u4f9b\u7535\u7cfb\u7edf\u6216\u8005\u5907\u7528\u7535\u6e90\uff1b\u5177\u5907\u65ad\u7535\u5c31\u8fd1\u81ea\u52a8\u5e73\u5c42\u5f00\u95e8\u529f\u80fd\u3002\u7535\u68af\u4f7f\u7528\u5355\u4f4d\u5e94\u4fdd\u6301\u7535\u68af\u8f7f\u53a2\u79fb\u52a8\u901a\u4fe1\u4fe1\u53f7\u8986\u76d6\uff0c\u914d\u5408\u57fa\u7840\u7535\u4fe1\u8fd0\u8425\u4f01\u4e1a\u53ca\u4fe1\u606f\u57fa\u7840\u8bbe\u65bd\u670d\u52a1\u4f01\u4e1a\u88c5\u8bbe\u79fb\u52a8\u901a\u4fe1\u8bbe\u65bd\u3002\uff08\u6765\u6e90\uff1a\u592e\u89c6\u65b0\u95fb\uff09"}, "attached_info": "CkYIo9aVgv6XqKVuEAMaCDU4ODM4NTM5IJ2c0v4FMAA4KEAFcgk0MzQ1MTc5NzZ4AKoBEWJpbGxib2FyZC1zY2llbmNl0gEA", "detail_text": "95 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": true, "children": [{"type": "answer", "thumbnail": ""}]}, {"type": "hot_list_feed", "style_type": "1", "id": "6_1607863181.8302915", "card_id": "Q_321322940", "target": {"id": 321322940, "title": "\u6709\u54ea\u4e9b\u4e8c\u7ea7\u7ed3\u8bba\u9002\u7528\u4e8e\u9ad8\u8003\u6570\u5b66\u4e2d\u7684\u9009\u62e9\u9898\u548c\u586b\u7a7a\u9898\uff1f", "url": "https://api.zhihu.com/questions/321322940", "type": "question", "created": 1555983174, "answer_count": 34, "follower_count": 490, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [1291, 31793, 73664], "comment_count": 0, "is_following": false, "excerpt": ""}, "attached_info": "CkcIo9aVgv6XqKVuEAMaCDMzNjgwOTE0IMbW+eUFMAA46gNABnIJMzIxMzIyOTQweACqARFiaWxsYm9hcmQtc2NpZW5jZdIBAA==", "detail_text": "90 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": false, "children": [{"type": "answer", "thumbnail": "https://picb.zhimg.com/50/v2-5825aeef9db7227306b79afb095ce79d_b.jpg"}]}, {"type": "hot_list_feed", "style_type": "1", "id": "7_1607863181.8305867", "card_id": "Q_269417463", "target": {"id": 269417463, "title": "\u4eba\u8111\u8fd0\u8f6c\u5230\u5e95\u6709\u6ca1\u6709\u91cf\u5b50\u529b\u5b66\u673a\u5236\uff1f", "url": "https://api.zhihu.com/questions/269417463", "type": "question", "created": 1521680182, "answer_count": 31, "follower_count": 462, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [350, 4433, 8437, 131409], "comment_count": 5, "is_following": false, "excerpt": "\u76ee\u524d\u4eba\u5de5\u667a\u80fd\u548c\u91cf\u5b50\u8ba1\u7b97\u706b\u7206\uff0c\u4eba\u8111\u667a\u80fd\u7684\u4f18\u8d8a\u6027\u53d7\u5230\u7a7a\u524d\u6311\u6218\u3002\u4f46\u5927\u89c4\u6a21\u7684\u91cf\u5b50\u8ba1\u7b97\u5b9e\u73b0\u8fd8\u5f88\u9065\u8fdc\uff0c\u5982\u679c\u4eba\u8111\u5343\u4ebf\u8ba1\u7684\u795e\u7ecf\u5143\u7684\u4fe1\u606f\u5904\u7406\u6a21\u5f0f\u7528\u5230\u4e86\u91cf\u5b50\u8ba1\u7b97\u7684\u673a\u5236\uff0c\u90a3\u5176\u4f18\u8d8a\u6027\u4e00\u5b9a\u8fd8\u80fd\u7ef4\u6301\u5f88\u4e45\u3002\u4f46\u95ee\u9898\u662f\u5230\u5e95\u4eba\u8111\u6709\u6ca1\u6709\u91cf\u5b50\u8ba1\u7b97\u4f5c\u4e3a\u5176\u8fd0\u884c\u673a\u5236\u5462\uff1f\u751f\u7269\u5b66\u4e0a\u6709\u4f55\u5b9a\u8bba\u5417\uff1f"}, "attached_info": "CkcIo9aVgv6XqKVuEAMaCDIyMTQ1Nzg1ILb+y9UFMAU4zgNAB3IJMjY5NDE3NDYzeACqARFiaWxsYm9hcmQtc2NpZW5jZdIBAA==", "detail_text": "87 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": false, "children": [{"type": "answer", "thumbnail": "https://pic3.zhimg.com/50/v2-1129458894e19dfe707d7760025db825_b.jpg"}]}, {"type": "hot_list_feed", "style_type": "1", "id": "8_1607863181.8309176", "card_id": "Q_325144561", "target": {"id": 325144561, "title": "\u535a\u58eb\u6700\u60e8\u80fd\u60e8\u5230\u4ec0\u4e48\u7a0b\u5ea6\uff1f", "url": "https://api.zhihu.com/questions/325144561", "type": "question", "created": 1558277284, "answer_count": 1251, "follower_count": 18899, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [1939, 5259, 12967, 61984, 93382], "comment_count": 56, "is_following": false, "excerpt": "\u53ef\u4ee5\u4ece\u8bfb\u535a\u671f\u95f4\u548c\u6bd5\u4e1a\u540e\u7684\u53d1\u5c55\u4e24\u65b9\u9762\u56de\u7b54\u3002"}, "attached_info": "CkgIo9aVgv6XqKVuEAMaCDM0NTMwMDMyIKTZhecFMDg405MBQAhyCTMyNTE0NDU2MXgAqgERYmlsbGJvYXJkLXNjaWVuY2XSAQA=", "detail_text": "81 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": false, "children": [{"type": "answer", "thumbnail": "https://pic3.zhimg.com/50/v2-2572d10cd8b89ae2b058aa9be6db3fa5_b.jpg"}]}, {"type": "hot_list_feed", "style_type": "1", "id": "9_1607863181.8312287", "card_id": "Q_31074747", "target": {"id": 31074747, "title": "\u672a\u6765\u795e\u7ecf\u79d1\u5b66\u53d1\u5c55\u7684\u65b9\u5411\u5728\u54ea\u91cc\uff1f", "url": "https://api.zhihu.com/questions/31074747", "type": "question", "created": 1433746261, "answer_count": 18, "follower_count": 721, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [419, 11898, 23174, 105575], "comment_count": 0, "is_following": false, "excerpt": "\u6211\u76ee\u524d\u5728ZJU\u8bfbneurobiology\u4e13\u4e1a\uff0c\u56e0\u4e3a\u4e4b\u524d\u4e00\u70b9\u6ca1\u63a5\u89e6\u8fc7\uff0c\u6240\u4ee5\u5bf9\u4e8e\u8fd9\u4e2a\u4e13\u4e1a\u7684\u53d1\u5c55\u65b9\u5411\u548c\u524d\u666f\u5f88\u96be\u628a\u63e1\u3002\u5bfc\u5e08\u5927\u591a\u662f\u7814\u7a76\u6291\u90c1\u75c7\u7b49\u75be\u75c5\u65b9\u5411\uff0c\u4e5f\u6709\u8bb0\u5fc6\u7b49\u9ad8\u7ea7\u529f\u80fd\u65b9\u9762\u3002\u4f46\u6211\u8bb0\u5f97ZJU\u8fd8\u6709\u4e2a\u6c42\u662f\u9ad8\u7b49\u7814\u7a76\u9662\uff0c\u8fd9\u91cc\u9762\u5305\u62ec\u795e\u7ecf\u3001\u8ba1\u7b97\u673a\u7b49\u4e13\u4e1a\uff0c\u4e3b\u8981\u7814\u7a76\u4eba\u8111\u63a5\u53e3\u3002\u6211\u6253\u7b97\u51fa\u56fd\u8bfb\u535a\uff0c\u4e0d\u77e5\u9053\u73b0\u5982\u4eca\uff0cneurobiology\u6216\u662fneuroscience\u7b49\u4e13\u4e1a\u70ed\u95e8\u7684\u65b9\u5411\u662f\u54ea\u4e9b\uff1f\u5c31\u4e1a\u524d\u666f\u600e\u4e48\u6837\uff1f\u4e5f\u60f3\u95ee\u95ee\uff0c\u5982\u4f55\u5c3d\u5feb\u4e86\u89e3\u8fd9\u4e00\u9886\u57df\uff0c\u8c22\u8c22\uff01(\u53e6\u5916\uff0c\u542c\u8bf4ZJU\u8fd9\u51e0\u5e74\u8fd9\u4e2a\u4e13\u4e1a\u5f88\u725b\uff0c\u4e0d\u77e5\u9053\u4e1a\u5185\u8bc4\u4ef7\u5982\u4f55\uff1f)"}, "attached_info": "CkUIo9aVgv6XqKVuEAMaBzQ2MTI0NzAg1fbUqwUwADjRBUAJcggzMTA3NDc0N3gAqgERYmlsbGJvYXJkLXNjaWVuY2XSAQA=", "detail_text": "64 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": false, "children": [{"type": "answer", "thumbnail": "https://pic3.zhimg.com/50/v2-497a1d6c18a69ebf92c452f26d662f81_b.jpg"}]}, {"type": "hot_list_feed", "style_type": "1", "id": "10_1607863181.8316612", "card_id": "Q_287426676", "target": {"id": 287426676, "title": "\u7406\u7efc\u7684\u9ad8\u9636\u601d\u7ef4\u662f\u4ec0\u4e48\uff0c\u5982\u4f55\u57f9\u517b\uff1f", "url": "https://api.zhihu.com/questions/287426676", "type": "question", "created": 1532840068, "answer_count": 170, "follower_count": 22510, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [119, 28850, 33929, 41299, 94719], "comment_count": 13, "is_following": false, "excerpt": "\u601d\u7ef4\u5bfc\u56fe\u521b\u59cb\u4eba\u4eb2\u6388\uff1a\u9ad8\u6548\u5b66\u4e60\u3001\u5de5\u4f5c\u7684\u601d\u8003\u672f"}, "attached_info": "CkgIo9aVgv6XqKVuEAMaCDI2MTQ5NzkzIISR9doFMA047q8BQApyCTI4NzQyNjY3NngAqgERYmlsbGJvYXJkLXNjaWVuY2XSAQA=", "detail_text": "59 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": false, "children": [{"type": "answer", "thumbnail": "https://pic2.zhimg.com/80/v2-449e4c1b201ed30cd0207b4f0706d4cd_hd.jpg"}]}, {"type": "hot_list_feed", "style_type": "1", "id": "11_1607863181.832112", "card_id": "Q_298738802", "target": {"id": 298738802, "title": "\u5982\u4f55\u505a\u4e00\u4e2a\u81ea\u5f8b\u7684\u4eba\u5462\uff1f", "url": "https://api.zhihu.com/questions/298738802", "type": "question", "created": 1539668089, "answer_count": 72, "follower_count": 758, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [800, 2537, 40758], "comment_count": 2, "is_following": false, "excerpt": "\u600e\u4e48\u6162\u6162\u57f9\u517b\u81ea\u5f8b\u7684\u4e60\u60ef\uff1f"}, "attached_info": "CkcIo9aVgv6XqKVuEAMaCDI4NjYyOTI2IPnwld4FMAI49gVAC3IJMjk4NzM4ODAyeACqARFiaWxsYm9hcmQtc2NpZW5jZdIBAA==", "detail_text": "59 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": true, "children": [{"type": "answer", "thumbnail": "https://pic3.zhimg.com/50/v2-15ce81eca1cd79d59b9b405dd2e5a4a9_b.jpg"}]}, {"type": "hot_list_feed", "style_type": "1", "id": "12_1607863181.8324335", "card_id": "Q_428394983", "target": {"id": 428394983, "title": "\u65e2\u7136\u7269\u8d28\u4e0d\u80fd\u51ed\u7a7a\u4ea7\u751f\uff0c\u90a3\u4e48\u5b87\u5b99\u6700\u521d\u7684\u7269\u8d28\u662f\u4ece\u54ea\u91cc\u6765\u7684\uff1f", "url": "https://api.zhihu.com/questions/428394983", "type": "question", "created": 1604248167, "answer_count": 380, "follower_count": 2202, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [20930, 23606, 25222], "comment_count": 38, "is_following": false, "excerpt": "\u5982\u9898 \u76ee\u524d\u79d1\u5b66\u754c\u6709\u6ca1\u6709\u76f8\u5173\u7406\u8bba"}, "attached_info": "CkcIo9aVgv6XqKVuEAMaCDU3NDc4MTMyIOfE+/wFMCY4mhFADHIJNDI4Mzk0OTgzeACqARFiaWxsYm9hcmQtc2NpZW5jZdIBAA==", "detail_text": "59 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": false, "children": [{"type": "answer", "thumbnail": "https://picb.zhimg.com/50/v2-4c8ae55222f92644506ca62952060223_b.jpg"}]}, {"type": "hot_list_feed", "style_type": "1", "id": "13_1607863181.8331957", "card_id": "Q_434428147", "target": {"id": 434428147, "title": "\u5982\u4f55\u770b\u5f85\u9ec4\u5188 24 \u6237\u5c45\u6c11\u7f51\u8d2d\u8fdb\u53e3\u51b7\u51bb\u732a\u8089\u88ab\u7f5a\uff0c\u5f53\u4e8b\u4eba\u88ab\u5355\u4f4d\u8981\u6c42\u8f9e\u804c\uff0c\u5b98\u65b9\u901a\u62a5\u300c\u64a4\u9500\u5904\u7f5a\u6df1\u8868\u6b49\u610f\u300d\uff1f", "url": "https://api.zhihu.com/questions/434428147", "type": "question", "created": 1607699333, "answer_count": 492, "follower_count": 2252, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [307, 2016, 130219, 566594, 583976], "comment_count": 81, "is_following": false, "excerpt": "\u3010\u6700\u65b0\u8fdb\u5c55\u301124\u540d\u5c45\u6c11\u7f51\u8d2d\u6d89\u75ab\u98df\u54c1\u88ab\u7f5a \u6e56\u5317\u9ec4\u5188\uff1a\u64a4\u9500\u5904\u7f5a\uff0c\u6df1\u8868\u6b49\u610f 12\u670812\u65e5\uff0c\u9ec4\u5188\u5e02\u9ec4\u5dde\u533a\u4eba\u6c11\u653f\u5e9c\u7f51\u7ad9\u53d1\u5e03\u300a\u5173\u4e8e\u9ec4\u5dde\u533a\u5c45\u6c11\u7f51\u8d2d\u6d89\u75ab\u8fdb\u53e3\u51b7\u94fe\u98df\u54c1\u540e\u7eed\u5904\u7f6e\u60c5\u51b5\u7684\u901a\u62a5\u300b\uff1a \u9488\u5bf9\u7f51\u53cb\u5173\u5fc3\u7684\u201c\u9ec4\u5dde\u533a\u5c45\u6c11\u8fdd\u89c4\u7f51\u4e0a\u91c7\u8d2d\u8fdb\u53e3\u51b7\u94fe\u98df\u54c1\u6392\u67e5\u5904\u7f6e\u60c5\u51b5\u7684\u901a\u62a5\u201d\uff0c\u73b0\u5c31\u6709\u5173\u540e\u7eed\u5904\u7f6e\u60c5\u51b5\u901a\u62a5\u5982\u4e0b: \u4e00\u300110\u670828\u65e5\u9ec4\u5dde\u533a\u75ab\u60c5\u9632\u63a7\u6307\u6325\u90e8\u53d1\u5e03\u7684\u7b2c27\u53f7\u901a\u544a\u4e2d\u5bf9\u4e2a\u4eba\u6240\u4f5c\u884c\u653f\u5904\u7f5a\uff0c\u5305\u62ec200\u5143\u7f5a\u6b3e\uff0c\u7531\u539f\u884c\u653f\u5904\u7f5a\u673a\u5173\u4e88\u4ee5\u64a4\u9500\u3002 \u4e8c\u3001\u6211\u533a\u5c06\u4e25\u683c\u843d\u5b9e\u7701\u5e02\u75ab\u60c5\u9632\u63a7\u6307\u6325\u90e8\u8981\u6c42\uff0c\u786e\u4fdd\u8fdb\u53e3\u51b7\u94fe\u98df\u54c1\u91c7\u6837\u5168\u8986\u76d6\u3001\u6837\u672c\u5168\u68c0\u6d4b\u3001\u5305\u88c5\u5168\u6d88\u6740\u3001\u5546\u54c1\u5168\u8ffd\u6eaf\uff0c\u575a\u51b3\u5835\u585e\u9632\u63a7\u6f0f\u6d1e\uff0c\u786e\u4fdd\u6d88\u8d39\u8005\u653e\u5fc3\u6d88\u8d39\u3002 \u4e09\u3001\u5bf9\u63a5\u89e6\u6d89\u75ab\u51b7\u94fe\u98df\u54c1\u76f8\u5173\u4eba\u5458\u5b9e\u884c\u514d\u8d39\u6838\u9178\u68c0\u6d4b\uff0c\u5e76\u843d\u5b9e\u597d\u5c45\u5bb6\u9694\u79bb\u89c2\u5bdf\u63aa\u65bd\u3002 \u5bf924\u540d\u5c45\u6c11\u5904\u7406\u4e0d\u5f53\uff0c\u6211\u4eec\u6df1\u8868\u6b49\u610f\uff0c\u8bda\u6073\u63a5\u53d7\u793e\u4f1a\u76d1\u7763\u3002\u6211\u4eec\u5c06\u5438\u53d6\u6559\u8bad\u3001\u4e3e\u4e00\u53cd\u4e09\uff0c\u4f9d\u6cd5\u4f9d\u89c4\u79d1\u5b66\u7cbe\u51c6\u505a\u597d\u5e38\u6001\u5316\u75ab\u60c5\u9632\u63a7\u5de5\u4f5c\u3002 \u5168\u6587\u8bf7\u6233\uff1a24\u540d\u5c45\u6c11\u7f51\u8d2d\u6d89\u75ab\u98df\u54c1\u88ab\u7f5a \u6e56\u5317\u9ec4\u5188\uff1a\u64a4\u9500\u5904\u7f5a\uff0c\u6df1\u8868\u6b49\u610f \u7b2c\u4e8c\u5929\uff0c\u4ed6\u628a\u6211\u4eec\u63a5\u89e6\u4e86\u6709\u6bd2\u75c5\u83cc\u7684\u8089\u8fd9\u4e2a\u6d88\u606f\u516c\u5e03\u5230\u6211\u5b69\u5b50\u7684\u5e7c\u513f\u56ed\u3001\u6211\u7684\u5355\u4f4d\uff0c\u6700\u540e\u641e\u5230\u5b66\u6821\u6253\u7535\u8bdd\u8fc7\u6765\uff0c\u6751\u91cc\u7684\u4eba\u89c1\u4e86\u6211\u4eec\u50cf\u89c1\u4e86\u9b3c\u4e00\u6837\uff0c\u6211\u548c\u6211\u8001\u5a46\u662f\u540c\u4e00\u4e2a\u5355\u4f4d\u7684\uff0c\u5355\u4f4d\u6253\u7535\u8bdd\u53eb\u6211\u592b\u59bb\u4fe9\u5199\u8f9e\u804c\u62a5\u544a\uff0c\u8fd9\u5bf9\u6211\u4eec\u7684\u4f24\u5bb3\u591a\u5927\uff01\u201d \u3010\u65b0\u95fb\u80cc\u666f\u3011 12\u67088\u65e5\uff0c\u6e56\u5317\u7701\u75ab\u60c5\u9632\u63a7\u6307\u6325\u90e8\u53d1\u5e03\u901a\u62a5\uff1a\u6b66\u6c49\u5e02\u5bf9\u6d2a\u5c71\u533a\u660c\u6676\u51b7\u94fe\u4ed3\u50a8\u4e2d\u5fc3\u8fdb\u53e3\u51b7\u94fe\u98df\u54c1\u8fdb\u884c\u65b0\u51a0\u75c5\u6bd2\u6838\u9178\u76d1\u6d4b\u68c0\u6d4b\u65f6\uff0c\u53d1\u73b0\u5df4\u897f\u8fdb\u53e3\u51b7\u51bb\u732a\u5c0f\u91cc\u810a\u80891\u4efd\u68c0\u6d4b\u7ed3\u679c\u5448\u9633\u6027\u3002 \u9ec4\u5188\u5e02\u9ec4\u5dde\u533a24\u6237\u5c45\u6c11\u901a\u8fc7\u7f51\u8d2d\u5e73\u53f0\u91c7\u8d2d\u4e0a\u8ff0\u540c\u6279\u6b21\u7684\u8fdb\u53e3\u51b7\u51bb\u732a\u5c0f\u91cc\u810a\u8089\u3002 \u622a\u81f312\u67089\u65e518\u65f6\uff0c\u5df2\u91c7\u96c6\u76f8\u5173\u4eba\u5458\u6837\u672c86\u4efd\u3001\u73af\u5883\u6837\u672c122\u4efd\uff0c\u68c0\u6d4b\u7ed3\u679c\u5747\u4e3a\u9634\u6027\u3002\u8be5\u533a\u5e02\u573a\u76d1\u7ba1\u90e8\u95e8\u5bf94\u6237\u8d2d\u4e70\u672a\u98df\u7528\u7684\u5df4\u897f\u8fdb\u53e3\u51b7\u51bb\u732a\u5c0f\u91cc\u810a\u8089\u5c01\u5b58\u9500\u6bc1\u3002 \u9ec4\u5dde\u516c\u5b89\u5206\u5c40\u5df2\u5bf9\u6d89\u4e8b\u7f51\u7edc\u5e73\u53f0\u9ec4\u5dde\u533a\u5408\u4f5c\u65b9\u8fdb\u884c\u7acb\u6848\uff0c\u4f9d\u6cd5\u4e25\u8083\u67e5\u5904\u3002\u5bf9\u8fdd\u89c4\u7f51\u4e0a\u91c7\u8d2d\u8fdb\u53e3\u98df\u54c1\u768424\u6237\u5c45\u6c11\uff0c\u81ea\u8d39\u627f\u62c5\u6838\u9178\u68c0\u6d4b\u8d39\u7528\u5e76\u843d\u5b9e\u5c45\u5bb6\u9694\u79bb\u63aa\u65bd\uff0c\u5f53\u5730\u516c\u5b89\u8fd8\u5bf9\u6bcf\u4eba\u7f5a\u6b3e200\u5143\u3002 \u5bf9\u6b64\uff0c\u9ec4\u5dde\u533a\u75ab\u60c5\u6307\u6325\u90e8\u56de\u5e94\u79f0\uff0c\u533a\u75ab\u60c5\u6307\u6325\u90e810\u670828\u65e5\u53d1\u5e03\u4e86\u901a\u544a\uff0c\u5168\u533a\u7981\u6b62\u91c7\u8d2d\u8fdb\u53e3\u51b7\u51bb\u8089\u54c1\uff0c\u5e76\u8fdb\u884c\u5e7f\u6cdb\u5ba3\u4f20\uff0c24\u6237\u5c45\u6c11\u8fdd\u53cd\u4e86\u6b64\u9879\u89c4\u5b9a\u3002 \u5bf9\u4e8e\u5904\u7f5a\u7f51\u8d2d\u51b7\u51bb\u91cc\u810a\u8089\u5c45\u6c11\u8fdb\u884c\u5904\u7f5a\u4e4b\u4e3e\uff0c\u8fc5\u901f\u5f15\u53d1\u4e89\u8bae\u3002 \u5168\u6587\u8bf7\u6233\uff1a"}, "attached_info": "CkcIo9aVgv6XqKVuEAMaCDU4ODE4NTY4IIWXzv4FMFE4zBFADXIJNDM0NDI4MTQ3eACqARFiaWxsYm9hcmQtc2NpZW5jZdIBAA==", "detail_text": "59 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": false, "children": [{"type": "answer", "thumbnail": "https://pic1.zhimg.com/80/v2-88f1cccb5aa2ae0e89968fd86c8271a2_720w.png"}]}, {"type": "hot_list_feed", "style_type": "1", "id": "14_1607863181.8342583", "card_id": "Q_50108447", "target": {"id": 50108447, "title": "\u9ad8\u4e2d\u7269\u7406\u53d7\u529b\u5206\u6790\u600e\u4e48\u753b?", "url": "https://api.zhihu.com/questions/50108447", "type": "question", "created": 1472383790, "answer_count": 35, "follower_count": 673, "author": {"type": "people", "user_type": "people", "id": "0", "url_token": "", "url": "", "name": "\u7528\u6237", "headline": "", "avatar_url": "https://pica.zhimg.com/aadd7b895_s.jpg"}, "bound_topic_ids": [4570, 28850, 93006, 105552], "comment_count": 13, "is_following": false, "excerpt": "\u9898\u4e3b\u51c6\u9ad8\u4e8c\uff0c\u5973\u751f\uff0c\u81ea\u4ece\u5b66\u4e86\u529b\u5b66\u7269\u7406\u6210\u7ee9\u76f4\u7ebf\u4e0b\u6ed1\uff0c\u6307\u6570\u7206\u70b8\u578b\u964d\u6210\u7ee9\u3002 \u53d7\u529b\u5206\u6790\u5b8c\u5168\u4e0d\u4f1a\uff0c\u770b\u89c1\u957f\u4e00\u70b9\u7684\u9898\u76ee\u5934\u90fd\u5927\u4e86\uff0c\u56fe\u590d\u6742\u4e00\u70b9\u66f4\u6ca1\u4fe1\u5fc3\u3002 \u516c\u5f0f\u90fd\u4f1a\uff0c\u4e0d\u4f1a\u7528\u3002\u505a\u9898\uff0c\u4e0d\u4f1a\u505a\u3002 \u6982\u5ff5\u7406\u4e86\u5f88\u591a\u6b21\uff0c\u4f46\u8fd8\u662f\u4e00\u5934\u96fe\u6c34\uff0c\u6c42\u63d0\u70b9\u3002 \u7269\u7406\u4e94\u5341\u5206\uff0c\u73ed\u5e73\u5747\u90fd\u4e0d\u5230\u3012_\u3012 \u8c22\u8c22\u89e3\u7b54\u3002"}, "attached_info": "CkYIo9aVgv6XqKVuEAMaCDEyMjYwMTQ2IK6Wi74FMA04oQVADnIINTAxMDg0NDd4AKoBEWJpbGxib2FyZC1zY2llbmNl0gEA", "detail_text": "54 \u4e07\u9886\u57df\u70ed\u5ea6", "trend": 0, "debut": false, "children": [{"type": "answer", "thumbnail": "https://pic2.zhimg.com/50/v2-f548ef2652c310a772bea4be0e65a67d_b.jpg"}]}], "paging": {"is_end": true, "next": "", "previous": ""}, "fresh_text": "\u70ed\u699c\u5df2\u66f4\u65b0"}'

real_data = json.loads(data)

print(real_data.keys())

for artical in real_data['data']:
    print(artical['target']['title'])
    print(artical['target']['author']['name'])