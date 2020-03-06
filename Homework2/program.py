from math import sqrt, sin, cos, asin, acos, atan2, pi
from matplotlib import pyplot as plt


def main():
    loop = [[0, 0], [0, 6], [10, 12], [10, 0]]
    A = 6
    B = sqrt(136)
    C = 12
    D = 10

    theta_a2 = acos(((A+B)**2 + D**2 - C**2)/(2*(A + B)*D))
    d = asin(D*sin(theta_a2)/C)
    b = pi - theta_a2 - d
    theta_c2 = 2*pi - b - d

    theta_a2 = rad_to_deg(theta_a2)
    d = rad_to_deg(d)
    b = rad_to_deg(b)
    theta_c2 = rad_to_deg(theta_c2)

    print("B = {}".format(round(B, 2)))
    print("theta_A = {0}, b = {1}, d = {2}".format(round(theta_a2, 2), round(b, 2), round(d, 2)))
    print("theta_C = {}".format(round(theta_c2, 2)))

    # print_loop(loop)
    # plt.show()

    theta_a = 90
    theta_b, theta_c = forward_kinematics(theta_a)
    b_point = get_b_central_coordinate(A, theta_a, B, theta_b)
    plot_links(theta_a, theta_b, theta_c)
    plt.plot(b_point[0], b_point[1], 'rx')
    plt.show()

    print()
    print("a = {0}, b = {1}, c = {2}".format(theta_a, theta_b, theta_c))

    plt.figure()
    angles = list(range(90, 370, 90))
    plot_lots_of_links(angles)

    angles = list(range(90, 460, 10))
    plot_b_central(angles, A, B)

    plt.plot([0, 10], [0, 0], "^")
    plt.title("Four-bar Rotated Through 360 Degrees\nin 10 Degree Increments")
    plt.legend([r'$\theta_A = 90$', r'$\theta_A = 180$', r'$\theta_A = 270$', r'$\theta_A = 360$', "Center of link B"])
    plt.xlabel("x position [cm]")
    plt.ylabel("y position [cm]")
    plt.axis("equal")
    plt.show()


def rad_to_deg(rad):
    return rad*180/pi


def deg_to_rad(deg):
    return deg*pi/180


def print_loop(vert_list: list):
    x_ords = []
    y_ords = []

    for coords in vert_list:
        x_ords.append(coords[0])
        y_ords.append(coords[1])

    # x_ords.append(vert_list[0][0])
    # y_ords.append(vert_list[0][1])

    plt.plot(x_ords, y_ords)


def forward_kinematics(a_deg):
    a = deg_to_rad(a_deg)
    sigma = 1
    LA = 6
    LB = sqrt(136)
    LC = 12
    LD = 10

    K1 = LD/LA
    K2 = LD/LC
    K3 = (LD**2 + LA**2 - LB**2 + LC**2)/(2*LA*LC)
    K4 = LD/LB
    K5 = (LD**2 + LA**2 + LB**2 - LC**2)/(2*LA*LB)

    A = K3 - K2*cos(a) + K1 - cos(a)
    B = 2*sin(a)
    C = K3 - K2*cos(a) - K1 + cos(a)
    D = K1 - K4*cos(a) + K5 - cos(a)
    E = 2*sin(a)
    F = -K1 - K4*cos(a) + K5 + cos(a)

    c = 2*atan2((-B + -sigma*sqrt(B**2 - 4*A*C)), 2*A)
    b = 2*atan2((-E + sigma*sqrt(E**2 - 4*D*F)), 2*D)

    return rad_to_deg(b), rad_to_deg(c)


def plot_links(a_deg, b_deg, c_deg):
    a = deg_to_rad(a_deg)
    b = deg_to_rad(b_deg)
    c = deg_to_rad(c_deg)
    loop = [[0, 0]]

    LA = 6
    LB = sqrt(136)
    LC = 12
    # LD = 10

    lengths = [LA, LB, LC]
    angles = [a, b, c]

    for L, x in zip(lengths, angles):
        last_coord = loop[-1]
        loop.append([L*cos(x) + last_coord[0], L*sin(x) + last_coord[1]])

    print_loop(loop)

    print(loop)


def get_b_central_coordinate(A, a_deg, B, b_deg):
    a = deg_to_rad(a_deg)
    b = deg_to_rad(b_deg)
    B_central = B/2

    A_coord = [A*cos(a), A*sin(a)]
    B_central_coord = [A_coord[0] + B_central*cos(b), A_coord[1] + B_central*sin(b)]
    return B_central_coord


def plot_b_central(angles: list, A, B):

    for theta_a in angles:
        theta_b, theta_c = forward_kinematics(theta_a)
        b_point = get_b_central_coordinate(A, theta_a, B, theta_b)
        plt.plot(b_point[0], b_point[1], 'rx')


def plot_lots_of_links(angles: list):

    for theta_a in angles:
        theta_b, theta_c = forward_kinematics(theta_a)
        plot_links(theta_a, theta_b, theta_c)


if __name__ == "__main__":
    main()
