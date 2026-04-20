import signal
import time

def timeout_handler(signum, frame):
    raise TimeoutError()

def timeout_decorator(timeout):
    def decorator(func):
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout)
        try:
            return func()
        finally:
            signal.alarm(0)
    return decorator

@timeout_decorator(5)  # 5 secondlar ichida timeout
def uzun_vaktsiz_funksiya():
    time.sleep(10)  # 10 secondlar davomida ishlash
    return "Funksiya tugallandi"

try:
    print(uzun_vaktsiz_funksiya())
except TimeoutError:
    print("Timeout: Funksiya 5 secondlar ichida tugallanmadi")
```

Kodda `signal` moduli qo'llaniladi, u quyidagi signalni qayta ishga tushirishga imkon beradi: `SIGALRM`. Bu signalni qayta ishga tushirish uchun `signal.alarm()` funksiyasi qo'llaniladi. `timeout_handler` funksiyasi `TimeoutError` istisno qo'yadi, agar signal qayta ishga tushirilganida. `timeout_decorator` funksiyasi `timeout` parametrini qabul qiladi va uni `decorator` funksiyasiga o'tkazadi. `decorator` funksiyasi `signal.signal()` funksiyasini qo'llaydi va `signal.alarm()` funksiyasini qo'llaydi. `uzun_vaktsiz_funksiya` funksiyasi `timeout_decorator` bilan qoplangan bo'lib, u 5 secondlar ichida tugallanmaganida `TimeoutError` istisno qo'yadi.
