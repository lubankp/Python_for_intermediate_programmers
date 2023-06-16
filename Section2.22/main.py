list = ["red", "orange", "green", "violet", "blue", "yellow"]


def generate_list(number):
    new_list = list.copy()[:number]
    return new_list


for i in range(1, len(list) + 1):
    print(generate_list(i))

text = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."

num1 = text.find("(") + 1
num2 = text.find(")")
subtext = text[num1:num2]
print(subtext)
