#ifndef _ABP
#define _ABP
#include <iostream>
#include <cstdlib>
#include <list>
using namespace std;

#include "NodoAB.h"

class BinarySearchTreeOfInteger
{
private:
  int count;
  NodoAB *root;
  void print(int height, NodoAB *aux);
  NodoAB* searchNodeRef(int elem, NodoAB *n);
  NodoAB* add(NodoAB* nodo, int element, NodoAB* father);
  void rotateLeft(NodoAB *desbalanceado);
  int balanceValue(NodoAB *nodo);
  void rotateRight(NodoAB *desbalanceado);
  list<int> positionsPre(NodoAB *n, list <int> &l);
  void balance(NodoAB *nodo);
  int height(NodoAB *n);
  int height(NodoAB *n, int h);
  void clear(NodoAB *n);
public:
    
    ~BinarySearchTreeOfInteger();
    BinarySearchTreeOfInteger();
    void print();
    bool isEmpty();
    int size();
    int getRoot();
    void add(int element);
    bool contains(int elem);
    NodoAB *getParent(int element);
    void clear();
    int height();
    BinarySearchTreeOfInteger clone();
    list<int> positionsPre();
    list<int> positionsCentral(); // implementar
    list<int> positionsPos(); // implementar
};
#endif
