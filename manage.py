#Імпортування проєкту
import Project

#Створення функції main, що запускає проект
def main():
    try:
        Project.project.run(debug = True)
    except Exception as error:
        print(error)

#Перевіряє що саме цей файл було запущено
if __name__ == '__main__':
    main()