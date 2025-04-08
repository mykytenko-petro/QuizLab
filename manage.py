#Імпортування проєкту
import Project

#Створення функції main
def main():
    try:
        Project.project.run(debug = True)
    except Exception as error:
        print(error)

#Запуск функції
if __name__ == '__main__':
    main()