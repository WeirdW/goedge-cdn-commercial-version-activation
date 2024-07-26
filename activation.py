import base64
import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

MagicKey = b"41100c93a65cfb71d5b0672c0d60d7ec"
MagicKey2 = b"70ba69d67bf7e61e17ac565c6093a325"[:16]

def create_cipher(key, iv):
    return Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())

def MagicKeyEncode(data):
    cipher = create_cipher(MagicKey, MagicKey2)
    encryptor = cipher.encryptor()
    return encryptor.update(data) + encryptor.finalize()

def MagicKeyDecode(data):
    cipher = create_cipher(MagicKey, MagicKey2)
    decryptor = cipher.decryptor()
    return decryptor.update(data) + decryptor.finalize()

def encrypt():
    _id = input("请输入ID（例如：commercial）：")
    hostname = input("请输入主机名（例如：*）：")
    company = input("请输入公司/组织名：")
    updated_at = int(input("请输入更新时间戳（例如：4102372799）："))
    nodes = int(input("请输入节点数量（例如：99999）：")
    edition = input("请输入版本（basic/pro/ent/maxsub/ultra）：")
    request_code = input("请输入请求代码（例如：F4BuVYEKSnnWucg5IDVzUWRFEJDPkunFObYNtXS4rxj3Bl+5rePM580nbSkizJoP3odKS1TTqWa3DDqaYDC59lhPuH147foFdmUOy6oR3X9dtBafw6cCRPplDaLTJ5RCEVVc4WHv3ja/lKd13HtTEYse3VHR+88KyShNDFBuqaNeSjA474Yb065yKWXNT+qs86/sWnr1GriLkYbSSLf85BHmTGL0qIfSUVzUOOlKg8XiTLsBtcXqdJa5x0Rw0p/9YcMUa/e2aZDvXqcXHP6Tc5pHXA873+wu/3PIiAKkwczD1M2KZ5C89hHlDpYRtNiIwD3wmB5F7f19jOT1ufg0On6xmcxmKiRgUoDbqsgh0x1tCvfYKS6IRKmCiAg2s/4TnheGWTa739sQEG7kJ7d5x3UgVOqy6p31l29AA5qOFkl8QtD2NMGVT21kHQ5f0Z/11z41YTYB1xhUetoxmyeEpAcPTCMB+c+OzDNGq1kZLUExIClGGFth）：")

    _json = {
        "id": _id,
        "dayFrom": "1999-01-01",
        "dayTo": "2099-12-31",
        "macAddresses": [],
        "requestCode": request_code,
        "hostname": hostname,
        "company": company,
        "nodes": nodes,
        "updatedAt": updated_at,
        "components": ["*"],
        "edition": edition,
        "email": "",
        "method": "local"
    }

    _json_str = json.dumps(_json, ensure_ascii=False).encode('utf-8')
    encoded = MagicKeyEncode(_json_str)

    print("\n↓原始JSON数据↓")
    print(_json_str.decode('utf-8'))
    print("\n↓注册码↓")
    print(base64.b64encode(encoded).decode())

    input("\n按回车键返回主菜单...")

def decrypt():
    encoded_str = input("请输入加密的注册码：")
    encoded_bytes = base64.b64decode(encoded_str)
    decoded_bytes = MagicKeyDecode(encoded_bytes)
    decoded_str = decoded_bytes.decode('utf-8')

    print("\n↓解密后的原始JSON数据↓")
    print(decoded_str)

    input("\n按回车键返回主菜单...") 

def main():
    while True:
        print("\n请选择操作：")
        print("1. 解密")
        print("2. 加密")
        print("0. 退出")
        choice = input("请输入选项 (1、2 或 0)：")

        if choice == "1":
            decrypt()
        elif choice == "2":
            encrypt()
        elif choice == "0":
            print("退出程序。")
            break
        else:
            print("无效的选项，请重新选择。")

if __name__ == "__main__":
    main()
