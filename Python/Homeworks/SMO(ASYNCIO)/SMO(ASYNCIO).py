import asyncio
queue = []
def spisok(number, people):
    for i in range(1, number + 1):
        people.append(i)
    return people

async def man(people, queue):
    await asyncio.sleep(1) #Интервал прихода нового человека
    if len(people) > 0:
        nick = people[0]
        print(f"Человек №{nick} зашел в магазин")
        if len(people)>0:
            people.pop(0)
        else:
            print("Магазин закрылся")
        print("Список людей снаружи после того, как один из них вошел внутрь =", people)
        print(f"Человек №{nick} больше не в уличной очереди")

        if len(queue) < 3:
            queue.append(nick)
            print(f"Человек №{nick} встает в очередь на кассу")
            print("Очередь после пополнения = ", queue)
        else:
            print(f"Человек №{nick} грустный уходит домой потому что ему лень стоять в очереди больше 3 людей")

async def service(queue):
    if len(queue)>0:
        print(f"Человек №{queue[0]} сейчас обслуживается") #1й человек не отображается как обслуживающийся
    await asyncio.sleep(3.5)  # время обслуживания
    if len(queue)>0:
        nick1 = queue[0]
        queue.pop(0)
        print(f"Человек №{nick1} больше не в очереди на кассу")
        print(f"Человек №{nick1} довольный уходит домой потому что купил покушать")
        print(f"Очередь после обслуживания человека №{nick1} =", queue)

async def main():
    # Schedule three calls *concurrently*:
    people =[]
    queue = []
    spisok(30, people)
    print(people)

    for name in range(1, len(people)+1):
         task1 = asyncio.create_task(man( people, queue))
         task2 = asyncio.create_task(man( people, queue))
         task3 = asyncio.create_task(man( people, queue))
         task4 = asyncio.create_task(service(queue))
         await task1
         await task2
         await task3
         await task4
    print("Магазин закрылся, люди снаружи разошлись по домам(Список людей снаружи закончился)")

if __name__ == "__main__":
     asyncio.run(main())
