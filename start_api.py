import uvicorn

def main():
    try:
        uvicorn.run(
            app= "api:app",
            reload= True,
            port = 3323
        )
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()