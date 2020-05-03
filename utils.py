import numpy as np
import cv2
def crop_img(img_path, row_start,col_start, width, height):
    img = cv2.imread(img_path)
    img=img[row_start:(row_start+height), col_start:(col_start+width)]
    cv2.imwrite(img_path, img)


def check_around_color(A):
    #input : 3x3
    kq=True
    # kq=(A[1,1]==A[0,0])
    kq=kq and (A[1,1]==A[0,1])
    # kq=kq and (A[1,1]==A[0,2])
    kq=kq and (A[1,1]==A[1,0])
    kq=kq and (A[1,1]==A[1,2])
    # kq=kq and (A[1,1]==A[2,0])
    kq=kq and (A[1,1]==A[2,1])
    # kq=kq and (A[1,1]==A[2,2])
    return kq
# A=np.array([[1,1,1],[1,1,1],[1,1,1]])
# print(check_around_color(A))

def find_cood_difference_color_in_image(file_path):
    img = cv2.imread(file_path, 2)
    nb_row = img.shape[0]
    nb_col = img.shape[1]


    dict_unique_color = {}
    dict_unique_color_coord = {}
    for i in range(1,nb_row-1,1):
        for j in range(1,nb_col-1,1):
            current_color = img[i, j]

            A=img[(i-1):(i+2), (j-1):(j+2)]
            if(check_around_color(A)):
                if not (current_color in dict_unique_color.keys()):
                    dict_unique_color[current_color] = 1
                    dict_unique_color_coord[current_color]=(i,j)
                else:
                    dict_unique_color[current_color] += 1


    A = list(dict_unique_color.values())
    A.sort()
    frequence_max_1 = A[-1]
    frequence_max_2 = A[-2]
    frequence_max_3 = A[-3]



    for key, value in dict_unique_color.items():
        if value == frequence_max_1:
            color_frequence_max_1 = key
        elif value == frequence_max_2:
            color_frequence_max_2 = key
        elif value == frequence_max_3:
            color_frequence_max_3 = key
        else:
            pass
    print(frequence_max_1, frequence_max_2, frequence_max_3)
    print(color_frequence_max_1, color_frequence_max_2, color_frequence_max_3)

    # is_search_coord_1 = True
    # is_search_coord_2 = True
    # is_search_coord_3 = True

    # for i in range(1,nb_row-1,1):
    #     for j in range(1,nb_col-1,1):
    #         current_color = img[i, j]
    #         A=img[(i-1):(i+2), (j-1):(j+2)]
            
    #         if(check_around_color(A)):
    #             if(is_search_coord_1 and color_frequence_max_1 == current_color):
    #                 # coord : background
    #                 print('xxx1xxxx:%s' % i, j)
    #                 is_search_coord_1 = False
    #             elif(is_search_coord_2 and color_frequence_max_2 == current_color):
    #                 # coord : majority color
    #                 print('xxx2xxxx:%s' % i, j)
    #                 is_search_coord_2 = False
    #                 # return (i, j)
    #             elif(is_search_coord_3 and color_frequence_max_3 == current_color):
    #                 # coord : result color
    #                 print('xxx3xxxx:%s' % i, j)
    #                 is_search_coord_3 = False
    #                 # return (i, j)
    #             else:
    #                 pass

    # print(dict_unique_color_coord[color_frequence_max_3])
    return dict_unique_color_coord[color_frequence_max_3]