import base64
a = "66y47KCc7J2YIOygleuLteydgA=="
s = "7JWM66Ck7KSEIOyImCDsl4bri6Q="
d = "7ZWY7KeA66eMIO2ejO2KuOuKlCDsnojri6Q="
t = "7Z6M7Yq464qUIGh0dHBzOi8vc3RhcnRsaW5rLmlvLyDsl5Ag7J6I64qUIOOFiOOFjuOFguOFjg=="
print(base64.b64decode(a).decode('utf-8'))
print(base64.b64decode(s).decode('utf-8'))
print(base64.b64decode(d).decode('utf-8'))
print(base64.b64decode(t).decode('utf-8'))