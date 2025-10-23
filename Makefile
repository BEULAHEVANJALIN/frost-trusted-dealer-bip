SECP=external/secp256k1lab
CC?=cc
CFLAGS=-O2 -Wall
INC=-I$(SECP)/include
LIB=$(SECP)/.libs/libsecp256k1.a

.PHONY: all vectors clean secp

all: tools/gen_vectors

sec p: $(LIB)

$(LIB):
	cd $(SECP) && ./autogen.sh && ./configure --enable-module-schnorrsig && make

tools/gen_vectors: tools/gen_vectors.c $(LIB)
	$(CC) $(CFLAGS) -o $@ $< $(INC) $(LIB)

vectors: tools/gen_vectors
	./tools/gen_vectors > tests/vectors/v1/frost_td_vectors.json

clean:
	rm -f tools/gen_vectors
