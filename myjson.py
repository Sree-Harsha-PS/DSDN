import json
NodeDetails = {
                "1" :{
                    "IP":"http://127.0.0.1:10001/",
                    "Status":"dead",
                },
                "2":{
                    "IP":"http://127.0.0.1:10002/",
                    "Status":"dead"
                },
                "3":{
                    "IP":"http://127.0.0.1:10003/",
                    "Status":"dead"
                },
                "4":{
                    "IP":"http://127.0.0.1:10004/",
                    "Status":"dead"
                },
                "5":{
                    "IP":"http://127.0.0.1:10005/",
                    "Status":"dead"
                },
                "6":{
                    "IP":"http://127.0.0.1:10006/",
                    "Status":"dead"
                },
                "7":{
                    "IP":"http://127.0.0.1:10007/",
                    "Status":"dead"
                },
                "8":{
                    "IP":"http://127.0.0.1:10008/",
                    "Status":"dead"
                },
                "9":{
                    "IP":"http://127.0.0.1:10009/",
                    "Status":"dead"
                },
                "10":{
                    "IP":"http://127.0.0.1:10010/",
                    "Status":"dead"
                },
                "11":{
                    "IP":"http://127.0.0.1:10011/",
                    "Status":"dead"
                },
                "12":{
                    "IP":"http://127.0.0.1:10012/",
                    "Status":"dead"
                },
                "13":{
                    "IP":"http://127.0.0.1:10013/",
                    "Status":"dead"
                },
                "14":{
                    "IP":"http://127.0.0.1:10014/",
                    "Status":"dead"
                },
                "15":{
                    "IP":"http://127.0.0.1:10015/",
                    "Status":"dead"
                },
                "16":{
                    "IP":"http://127.0.0.1:10016/",
                    "Status":"dead"
                },
                "17":{
                    "IP":"http://127.0.0.1:10017/",
                    "Status":"dead"
                },
                "18":{
                    "IP":"http://127.0.0.1:10018/",
                    "Status":"dead"
                },
                "19":{
                    "IP":"http://127.0.0.1:10019/",
                    "Status":"dead"
                },
                "20":{
                    "IP":"http://127.0.0.1:10020/",
                    "Status":"dead"
                },
                "21":{
                    "IP":"http://127.0.0.1:10021/",
                    "Status":"dead"
                },
                "22":{
                    "IP":"http://127.0.0.1:10022/",
                    "Status":"dead"
                },
                "23":{
                    "IP":"http://127.0.0.1:10023/",
                    "Status":"dead"
                },
                "24":{
                    "IP":"http://127.0.0.1:10024/",
                    "Status":"dead"
                },
                "25":{
                    "IP":"http://127.0.0.1:10025/",
                    "Status":"dead"
                },
                "26":{
                    "IP":"http://127.0.0.1:10026/",
                    "Status":"dead"
                },
                "27":{
                    "IP":"http://127.0.0.1:10027/",
                    "Status":"dead"
                },
                "28":{
                    "IP":"http://127.0.0.1:10028/",
                    "Status":"dead"
                },
                "29":{
                    "IP":"http://127.0.0.1:10029/",
                    "Status":"dead"
                },
                "30":{
                    "IP":"http://127.0.0.1:10030/",
                    "Status":"dead"
                }
            }


print(NodeDetails["1"])
jsonData = json.dumps(NodeDetails)

print(type(jsonData))
data = json.loads(jsonData)
print(data["1"])