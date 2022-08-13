import json
import requests

def main():
    url = "http://127.0.0.1:7777"
    data = {"text":"Google LLC は、検索エンジン技術、オンライン広告、クラウド コンピューティング、コンピューター ソフトウェア、量子コンピューティング、e コマース、人工知能、家電製品に焦点を当てたアメリカの多国籍テクノロジー企業です","lang":"en"}
    r = requests.get(url,params=data)
    output = r.json()
    print(output)



if __name__ == '__main__':
    main()
