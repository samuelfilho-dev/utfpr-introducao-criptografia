 #include <stdlib.h>
 #include <stdio.h>
 #include <string.h>
 #include <math.h>
 
 #define USAGE    "Usage: sdes <-e | -d> <input file> <output file> <key 0-1023> <IV 0-255>\n"
 
 #define BIT_1    1
 #define BIT_2    2
 #define BIT_3    4
 #define BIT_4    8
 #define BIT_5    16
 #define BIT_6    32
 #define BIT_7    64
 #define BIT_8    128
 #define BIT_9    256
 #define BIT_10   512
 
 #define BITMASK_RIGHT    (BIT_1 | BIT_2 | BIT_3 | BIT_4)
 
 //#define DBG(desc, num, bits)    dbg_num(desc, num, bits);
 #define DBG(desc, num, bits)        //
 
 static short int sbox0[][4] = {
								 1, 0, 3, 2,
								 3, 2, 1, 0,
								 0, 2, 1, 3,
								 3, 1, 3, 2
							   };
 static short int sbox1[][4] = {
								 0, 1, 2, 3,
								 2, 0, 1, 3,
								 3, 0, 1, 0,
								 2, 1, 0, 3
							   };
 
 void display_bits(int num, int bits) {
	 unsigned int i;
 
	 if(bits < 1 || bits > 32) {
		 printf("Invalid bit quantity");
		 return;
	 }
	 /* display binary representation */
	 for(i = pow(2, bits-1); i > 0; i = i / 2) {
		 printf("%s",(i & num) ? "1" : "0");
	 }
	 printf("\n");
 }
 
 void dbg_num(char *desc, int num, int bits) {
	 printf("%s", desc);
	 display_bits(num, bits);
 }
 
 /**
  * F function used by Fk algorithm. Input are the 4-bits to convert and a subkey.
  * It performs an expansion/permutation, xor with subkey and sbox mapping + permutation
  *
  * @param input  4-bits
  * @param sk  subkey to combine
  */
 static char f(char input, char sk) {
	 short int row0=0,col0=0,row1=0,col1=0;
	 char out='\0',ep='\0',aux='\0';
 
	 DBG("f() input: ", (int)input, 8);
 
	 // E/P
	 aux = !!(input & BIT_1);
	 ep |= ((aux << 7) | (aux << 1));
	 aux = !!(input & BIT_2);
	 ep |= ((aux << 4) | (aux << 2));
	 aux = !!(input & BIT_3);
	 ep |= ((aux << 5) | (aux << 3));
	 aux = !!(input & BIT_4);
	 ep |= ((aux << 6) | aux);
	 DBG("E/P: ", (int)ep, 8);
 
	 // xor with subkey
	 ep = ep ^ sk;
	 DBG("E/P ^ sk: ", (int)ep, 8);
 
	 // calculate row and columns for sboxes
	 row0 = !!(ep & BIT_8);
	 row0 = (row0 << 1) | !!(ep & BIT_5);
	 col0 = !!(ep & BIT_7);
	 col0 = (col0 << 1) | !!(ep & BIT_6);
	 row1 = !!(ep & BIT_4);
	 row1 = (row1 << 1) | !!(ep & BIT_1);
	 col1 = !!(ep & BIT_3);
	 col1 = (col1 << 1) | !!(ep & BIT_2);
 
	 // P4 (2,4,3,1)
	 out = !!(sbox0[row0][col0] & BIT_1);
	 out = (out << 1) | !!(sbox1[row1][col1] & BIT_1);
	 out = (out << 1) | !!(sbox1[row1][col1] & BIT_2);
	 out = (out << 1) | !!(sbox0[row0][col0] & BIT_2);
	 DBG("f() out: ", (int)out, 8);
 
	 return(out);
 }
 
 /**
  * Main Fk complex algorithm
  *
  * @param input  byte to apply Fk algorithm
  * @param sk1  first subkey
  * @param sk2  second subkey
  */
 static char fk(char input, char sk1, char sk2) {
	 char l='\0',r='\0',out='\0';
 
	 DBG("Fk IN: ", (int)input, 8);
	 // first 4 bits
	 r = (input & BITMASK_RIGHT);
	 l = (input >> 4);
	 out = ((f(r, sk1) ^ l) & BITMASK_RIGHT) | (r << 4);        // the output is switched here
	 DBG("Fk OUT + Swap: ", (int)out, 8);
	 // second 4 bits
	 r = (out & BITMASK_RIGHT);
	 l = (out >> 4);
	 out = ((f(r, sk2) ^ l) << 4) | r;
	 DBG("Fk OUT: ", (int)out, 8);
	 return(out);
 }
 
 /**
  * Generate two 8-bit subkeys based on a 10-bit key
  *
  * @param key  10-bit key
  * @param sk1  pointer that receives the first subkey
  * @param sk2  pointer that receives the second subkey
  */
 static void generate_sub_keys(short int key, char *sk1, char *sk2) {
	 short int i;
	 short int k1_order[] = { BIT_10, BIT_4, BIT_2, BIT_7, BIT_3, BIT_8, BIT_1, BIT_5 };
	 short int k2_order[] = { BIT_3, BIT_8, BIT_5, BIT_6, BIT_1, BIT_9, BIT_2, BIT_10 };
 
	 *sk1 = '\0';
	 *sk2 = '\0';
	 for (i = 0; i < 8; i++) {
		 *sk1 = (*sk1 << 1) | !!(k1_order[i] & key);
		 *sk2 = (*sk2 << 1) | !!(k2_order[i] & key);
	 }
 }
 
 /**
  * Initial permutation
  *
  * @param byte  input to apply the permutation
  */
 static char ip(char byte) {
	 short int i;
	 char ret;
	 short int order[] = { BIT_7, BIT_3, BIT_6, BIT_8, BIT_5, BIT_1, BIT_4, BIT_2 };
 
	 ret = '\0';
	 for (i = 0; i < 8; i++) {
		 ret = (ret << 1) | !!(order[i] & byte);
	 }
	 return(ret);
 }
 
 /**
  * Initial permutation inverted
  *
  * @param byte  input to apply the inverted permutation
  */
 static char ip_inverse(char byte) {
	 short int i;
	 char ret;
	 short int order[] = { BIT_5, BIT_8, BIT_6, BIT_4, BIT_2, BIT_7, BIT_1, BIT_3 };
 
	 ret = '\0';
	 for (i = 0; i < 8; i++) {
		 ret = (ret << 1) | !!(order[i] & byte);
	 }
	 return(ret);
 }
 
 /**
  * Main program entry point
  */
 int main (int argc, const char* argv[]) {
	 short int key;
	 char iv;
	 char sk1, sk2;
 
	 if (argc != 6) {
		 printf(USAGE);
		 return(1);
	 }
  
	 FILE *in_file = fopen(argv[2], "rb");
	 if (!in_file) {
		 printf("File not found %s\n", argv[2]);
		 return(1);
	 }
 
	 FILE *out_file = fopen(argv[3], "wb+");
	 if (!out_file) {
		 printf("Error creating output file %s\n", argv[3]);
		 fclose(in_file);
		 return(1);
	 }
 
	 key = atoi(argv[4]);
	 iv = (char)atoi(argv[5]);
   
	 if ((key < 0 || key > 1023) || strlen(argv[1]) != 2 || argv[1][0] != '-') {
		 printf(USAGE);
		 return(1);
	 }
 
	 key = (key % 1024);
	 iv = iv % 256;
 
	 if (strcmp(argv[1],"-e") == 0) { /*encryption*/
		 char prev_cipher = iv;
		 char plaintext, ciphertext;
		 
		 generate_sub_keys(key, &sk1, &sk2);
		 printf("Processing encryption in CBC mode...\n");
		 
		 while (!feof(in_file)) {
			 /* reading character */
			 fscanf(in_file, "%c", &plaintext);
			 if (!feof(in_file)) {
				 /* XOR with previous ciphertext (or IV for first block) */
				 plaintext ^= prev_cipher;
				 
				 /* initial permutation (ip) */
				 plaintext = ip(plaintext);
				 
				 /* apply function Fk */
				 ciphertext = fk(plaintext, sk1, sk2);
				 
				 /* ip^-1 */
				 ciphertext = ip_inverse(ciphertext);
				 
				 /* save ciphertext for next block */
				 prev_cipher = ciphertext;
				 
				 /* write ciphertext */
				 fprintf(out_file, "%c", ciphertext);
			 }
		 }
	 }
	 else if (strcmp(argv[1],"-d") == 0) { /*decryption*/
		 char prev_cipher = iv;
		 char ciphertext, plaintext;
		 
		 generate_sub_keys(key, &sk2, &sk1);
		 printf("Processing decryption in CBC mode...\n");
		 
		 while (!feof(in_file)) {
			 /* reading character */
			 fscanf(in_file, "%c", &ciphertext);
			 if (!feof(in_file)) {
				 char temp = ciphertext; // Save for XOR after decryption
				 
				 /* initial permutation (ip) */
				 ciphertext = ip(ciphertext);
				 
				 /* apply function Fk */
				 plaintext = fk(ciphertext, sk1, sk2);
				 
				 /* ip^-1 */
				 plaintext = ip_inverse(plaintext);
				 
				 /* XOR with previous ciphertext (or IV for first block) */
				 plaintext ^= prev_cipher;
				 
				 /* update previous ciphertext for next block */
				 prev_cipher = temp;
				 
				 /* write plaintext */
				 fprintf(out_file, "%c", plaintext);
			 }
		 }
	 }
	 else {
		 printf(USAGE);
		 return(1);
	 }
 
	 printf("Ready!\n");
	 fclose(in_file);
	 fclose(out_file);
	 return 0;
 }