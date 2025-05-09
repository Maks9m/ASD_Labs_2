# Постановка задачi
## 1. Представити зважений ненапрямлений граф iз заданими параметрами так само, як у лабораторнiй роботi №3. 
Вiдмiннiсть 1: коефiцiєнт k = 1.0 - n3 * 0.01 - n4 * 0.005 - 0.05.  Отже, матриця сумiжностi Adir напрямленого графа за варiантом формується таким чином:
1) встановлюється параметр (seed) генератора випадкових чисел, рiвне номеру варiанту n1n2n3n4;
2) матриця розмiром n * n заповнюється згенерованими випадковими числами в дiапазонi [0, 2.0);
3) обчислюється коефiцiєнт k = 1.0 - n3 * 0.01 - n4 * 0.005 - 0.05, кожен елемент матрицi множиться на коефiцiєнт k;
4) елементи матрицi округлюються: 0 — якщо елемент менший за 1.0, 1 — якщо елемент бiльший або дорiвнює 1.0. Матриця Aundir ненапрямленого графа одержується з матрицi Adir так само, як у ЛР №3.

Вiдмiннiсть 2: матриця ваг W формується таким чином.
1) матриця B розмiром n * n заповнюється згенерованими випадковими числами в дiапазонi [0, 2.0) (параметр генератора випадкових чисел той же самий, n1n2n3n4);
2) одержується матриця C:
c(i,j) = ceil(b(i,j) * 100 * aundir(i,j))   c(i,j) Є C, b(i,j) Є B, Aundir(i,j) Є Aundir, де ceil — це функцiя, що округляє кожен елемент матрицi до найближчого цiлого числа, бiльшого чи рiвного за дане;
3) одержується матриця D, у якiй
d(i,j) = 0, якщо c(i,j) = 0,
d(i,j) = 1, якщо c(i,j) > 0, d(i,j) Є D, c(i,j) Є C;
4) одержується матриця H, у якiй
h(i,j) = 1, якщо d(i,j) ≠ d(j,i),
та h(i,j) = 0 в iншому випадку;
5) Tr — верхня трикутна матриця з одиниць (tr(i,j) = 1 при i < j);
6) матриця ваг W симетрична, i її елементи одержуються за формулою: w(i,j) = w(j,i) = (d(i,j) + h(i,j) * tr(i,j)) * c(i,j).

## 2. Створити програму для знаходження мiнiмального кiстяка за алгоритмом Краскала при n4 — парному i за алгоритмом Прiма — при непарному. При цьому у програмi:
- графи представляти у виглядi динамiчних спискiв, обхiд графа, додавання, вiднiмання вершин, ребер виконувати як функцiї з вершинами вiдповiдних спискiв;
- у програмi виконання обходу вiдображати покроково, черговий крок виконувати за натисканням кнопки у вiкнi або на клавiатурi.

## 3. Пiд час обходу графа побудувати дерево його кiстяка. У програмi дерево кiстяка виводити покроково у процесi виконання алгоритму. Це можна виконати одним iз двох способiв:
- або видiляти iншим кольором ребра графа;
- або будувати кiстяк поряд iз графом.
При зображеннi як графа, так i його кiстяка, вказати ваги ребер.

## При проєктуваннi програми також слiд врахувати наступне:
1) мова програмування обирається студентом самостiйно;
2) графiчне зображення усiх графiв має формуватися програмою з тими ж вимогами, як у ЛР №3;
3) всi графи обов’язково зображувати у графiчному вiкнi;
4) типи та структури даних для внутрiшнього представлення всiх даних у програмi слiд вибрати самостiйно.
