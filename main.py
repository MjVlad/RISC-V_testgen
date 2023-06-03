from src.Generator import Generator

if __name__ == '__main__':
    path = 'C:\\Учёба\\diplom\\'
    print('start')
    generator = Generator()
    file = open(path + 'test_out.S', 'w')
    file.write(generator.gen_code(1000))
    file.close()
    print('end')
