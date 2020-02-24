from smbus import SMBus


def main():
    b = SMBus(1)
    b.read_byte_data(0x2f, 0x58)


if __name__ == '__main__':
    main()


