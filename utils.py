import cv2
def crop_img(img_path, row_start,col_start, width, height):
    img = cv2.imread(img_path)
    img=img[row_start:(row_start+height), col_start:(col_start+width)]
    cv2.imwrite(img_path, img)
    
def find_cood_difference_color_in_image(file_path):
    img = cv2.imread(file_path, 0)
    nb_row = img.shape[0]
    nb_col = img.shape[1]

    # print(nb_row, nb_col)

    dict_unique_color = {}
    for i in range(0,nb_row,5):
        for j in range(0,nb_col,5):
            current_color = img[i, j]
            if not (current_color in dict_unique_color.keys()):
                dict_unique_color[current_color] = 1
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

    is_search_coord_1 = True
    is_search_coord_2 = True
    is_search_coord_3 = True
    for i in range(0, nb_row, 5):
        for j in range(0,nb_col,5):
            current_color = img[i, j]
            if(is_search_coord_1 and color_frequence_max_1 == current_color):
                # coord : background
                print('xxx1xxxx:%s' % i, j)
                is_search_coord_1 = False
            elif(is_search_coord_2 and color_frequence_max_2 == current_color):
                # coord : majority color
                print('xxx2xxxx:%s' % i, j)
                is_search_coord_2 = False
                # return (i, j)
            elif(is_search_coord_3 and color_frequence_max_3 == current_color):
                # coord : result color
                print('xxx3xxxx:%s' % i, j)
                is_search_coord_3 = False
                return (i, j)
            else:
                pass
