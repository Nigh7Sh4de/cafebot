$ 7z a cafebot.zip ./deps/* cafebot.py

$ aws lambda update-function-code --function-name Cafebot --zip-file fileb://cafebot.zip
