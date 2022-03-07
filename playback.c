#include <stdio.h>
#include "data.h"

#ifdef WIN32
#include <windows.h>
#else
#endif
#include <unistd.h>

#define CHAR_CNT 7
#define NODE_CNT (CHAR_CNT + CHAR_CNT - 1)

#define WIDTH 80
#define HEIGHT 22
#define FPS 15

#define FRAME_SIZE ((WIDTH + 1) * HEIGHT + 1)

const char* char_set = " ,(S#g@";

char frame[FRAME_SIZE];

int prediction_matrix[CHAR_CNT][CHAR_CNT];
int huffman_tree_left[NODE_CNT];
int huffman_tree_right[NODE_CNT];

int data_pos = 0;

int next_char() {
  if(data_pos < data_len) {
      return data[data_pos++];
  }

  return EOF;
}

int peek_char() {
  if(data_pos < data_len) {
      return data[data_pos];
  }

  return EOF;
}

void decode_matrix_row(int row, int row_data) {
    int idxs[CHAR_CNT];

    for(int i = 0; i < CHAR_CNT; i++) {
        idxs[i] = i;
    }
    
    for(int i = 0; i < CHAR_CNT; i++) {
        int idx = row_data % (CHAR_CNT - i);
        int rank = idxs[idx];
        row_data /= (CHAR_CNT - i);

        // Shift all the idxs over by one
        for(int j = idx; j < CHAR_CNT - 1; j++) {
            idxs[j] = idxs[j + 1];
        }

        prediction_matrix[row][i] = rank;
    }
}

void decode_tree() {
    for(int i = 0; i < CHAR_CNT - 1; i++) {
        int c = next_char();

        int left = c / 16;
        int right = c % 16;

        huffman_tree_left[i + CHAR_CNT] = left;
        huffman_tree_right[i + CHAR_CNT] = right;
    }
}

void decode_frame() {
    int bit_cnt = 0;
    int c = 0;

    // Start our node at the root of the tree
    int node = NODE_CNT - 1;
    int last_char = 0;

    int out_pos = 0;

    int out_cnt = 0;
    int line_cnt = 0;

    while(1) {
        if(bit_cnt == 0) {
            c = next_char();
            bit_cnt = 8;
        }

        if(c == EOF) return;

        int bit = c & 0b10000000;
        c <<= 1;
        bit_cnt -= 1;
        

        node = (bit > 0) ? huffman_tree_right[node] : huffman_tree_left[node];

        if(node < CHAR_CNT) {
            last_char = prediction_matrix[last_char][node];
            
            frame[out_pos++] = char_set[last_char];

            out_cnt++;
            if(out_cnt >= WIDTH) {
                out_cnt = 0;
                
                line_cnt++;

                if(line_cnt >= HEIGHT) {
                    frame[out_pos++] = '\0';
                    return;
                }
            }

            node = NODE_CNT - 1;
        }
    }
    

}

int main() {

    // Null terminate the string
    frame[FRAME_SIZE - 1] = '\0';

    #ifdef WIN32
    COORD coord;
    coord.X = 0;
    coord.Y = 0;

    HANDLE hConsole = GetStdHandle(STD_OUTPUT_HANDLE);
    #endif

    do {
        for(int row = 0; row < CHAR_CNT; row++) {
            int row_data = (next_char() * 256) + next_char();
            decode_matrix_row(row, row_data);
        }

        decode_tree();
        decode_frame();

        #ifdef WIN32
        SetConsoleCursorPosition(hConsole, coord);
        printf("%s", frame);
        Sleep(1000 / FPS);
        #else
        printf("%s\n", frame);
        usleep(1000000 / FPS);
        #endif


    } while(peek_char() != EOF);

    return 0;
}