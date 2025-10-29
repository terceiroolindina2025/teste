from datetime import datetime

def main():
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"Script executado automaticamente às {agora} ⏰")

if __name__ == "__main__":
    main()
