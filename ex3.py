import os
import string

def count_words(file_name):
    output_file = "q1_output.txt"
    with open(file_name, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            words = [word for word in line.split() if len(word.strip(string.punctuation)) >= 3 and word.isalpha()]
            outfile.write(f"{len(words)}\n")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def twin_pricks(num):
    output_file = f"q2a_output_{num}.txt"
    twin_primes = []
    candidate = 2
    while len(twin_primes) < num:
        if is_prime(candidate) and is_prime(candidate + 2):
            twin_primes.append((candidate, candidate + 2))
        candidate += 1
    with open(output_file, 'w') as outfile:
        for idx, (p1, p2) in enumerate(twin_primes, start=1):
            outfile.write(f"{idx}. {p1}-{p2}\n")

def K_boom(n, k):
    output_file = f"q2b_output_{k}_boom_{n}.txt"
    with open(output_file, 'w') as outfile:
        for i in range(1, n + 1):
            divisible = (i % k == 0)
            contains = (str(k) in str(i))
            if divisible and contains:
                outfile.write("boom-boom\n")
            elif divisible or contains:
                outfile.write("boom\n")
            else:
                outfile.write(f"{i}\n")

def decipher_rotate(in_file):
    def rotate_char(c):
        if c.isalpha():
            is_upper = c.isupper()
            base = ord('A') if is_upper else ord('a')
            rotated = base + (25 - (ord(c) - base + 5) % 26)
            return chr(rotated)
        return c

    out_file = os.path.splitext(in_file)[0] + "_decipherotate.txt"
    with open(in_file, 'r') as infile, open(out_file, 'w') as outfile:
        for line in infile:
            decoded = ''.join(rotate_char(c) for c in line)
            outfile.write(decoded)
    return out_file

def analyze_student_scores(students_ids, students_scores):
    students = {}
    with open(students_ids, 'r') as id_file:
        for line in id_file:
            student_id, name = line.strip().split(',')
            students[student_id] = (name, [])

    with open(students_scores, 'r') as scores_file:
        for line in scores_file:
            student_id, score = line.strip().split(',')
            if student_id in students:
                students[student_id][1].append(int(score))

    return {k: (v[0], v[1]) for k, v in students.items()}

# Example function calls
# count_words("Winnie_the_Pooh.txt")
# twin_pricks(5)
# K_boom(15, 7)
# decipher_rotate("example.txt")
# analyze_student_scores("students_ids.txt", "students_scores.txt")
