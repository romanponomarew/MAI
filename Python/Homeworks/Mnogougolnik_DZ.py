# Алгоритм Джарвиса - поиск следующей точки по минимальному углу
# Класс Point для координат x,y точек
class Point:
      def __init__(self, x, y):
            self.x = x
            self.y = y


def Left_index(points):
      # Функция поиска самой левой точки, точки начала построения
      minn = 0
      for i in range(1, len(points)):
            if points[i].x < points[minn].x:
                  minn = i
            elif points[i].x == points[minn].x: #При равных x левой точки ищем самую левую, верхнюю точку
                  if points[i].y > points[minn].y:
                        minn = i
      return minn


def orientation(p, q, r):
      '''
      Расчет правой тройки векторов, направление построения по алгоритму - против часовой стрелки (p, q, r).
      Функция возвращает 0, 1 или 2:
      0 --> p, q и r - параллельны
      1 --> левая тройка векторов (по часовой стрелке)
      2 --> правая тройка векторов (против часовой стрелки)
      '''
      val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)

      if val == 0:
            return 0
      elif val > 0:
            return 1
      else:
            return 2

def convexHull(points, n):
      # Должно быть по крайней мере 3 точки
      if n < 3:
            return

      # Находим самую левую точку для начала построения
      l = Left_index(points)

      hull = []

      ''' 
      Начинаем с левой точки, двигаясь против часовой стрелки пока не попадем в начальную точку
      '''
      p = l
      q = 0
      while (True):

            # Добавляем текущую точку к результату
            hull.append(p)
            ''' 
            Ищем точку q, которая правее текущей точки. Если точка i правее, чем q - изменяем q
            '''
            q = (p + 1) % n

            for i in range(n):
                  # If i is more counterclockwise
                  # than current q, then update q
                  if (orientation(points[p], points[i], points[q]) == 2):
                        q = i
            ''' 
            Now q is the most counterclockwise with respect to p  
            Set p as q for next iteration, so that q is added to  
            result 'hull'  
            '''
            p = q
            # Пока не вернемся в начальную точку
            if (p == l):
                  break
      # Вывод результата
      for each in hull:
            print(points[each].x, points[each].y)

      # Входные данные
points = []
points.append(Point(1, 2))
points.append(Point(2, 2))
points.append(Point(2, 0))
points.append(Point(0, 1))
points.append(Point(3, 4))
points.append(Point(0, 3))
points.append(Point(3, 3))
points.append(Point(3, 5))
convexHull(points, len(points))
# Python1
