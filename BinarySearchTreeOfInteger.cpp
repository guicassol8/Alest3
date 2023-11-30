#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

#include "BinarySearchTreeOfInteger.h"

BinarySearchTreeOfInteger::BinarySearchTreeOfInteger() {
    root = NULL;
    count = 0;
}

/* Verifica se a arvore esta vazia ou nao */
bool BinarySearchTreeOfInteger::isEmpty() {
    return (root == NULL);
}

/* Retorna o total de elementos da arvore. */
int BinarySearchTreeOfInteger::size() {
    return count;
}

/* Retorna o elemento armazenado na raiz da arvore. */
int BinarySearchTreeOfInteger::getRoot() {
    if (isEmpty()) {
        throw 0;
    }
    return root->element;
}




// Metodo privado que procura por element a partir de n
// e retorna a referencia para o nodo no qual elem esta
// armazenado.
NodoAB* BinarySearchTreeOfInteger::searchNodeRef(int element, NodoAB *nodo) {
    
    if (nodo == NULL) // não achou!
        return NULL;
    
    if (nodo->element == element) // achou!
        return nodo;
    
    if (element < nodo->element) // Se o elemento buscado é menor que o nodo atual
        return searchNodeRef (element, nodo->left); // então, busca à esquerda
    else
        return searchNodeRef (element, nodo->right); // senão, busca à direita
    
    return NULL;
}

/* Verifica se element esta ou nao armazenado na arvore. */
bool BinarySearchTreeOfInteger::contains(int elem) {
   NodoAB *nAux = searchNodeRef(elem, root);
   return (nAux != NULL);
}

void BinarySearchTreeOfInteger::print(){
    print(0, root);
    return;
}

void BinarySearchTreeOfInteger::print(int height, NodoAB *aux){
    string tracinhos;
    for(int i = 0; i < height; i++){
        tracinhos.append("-");
    }
    if(aux != NULL)
        cout << tracinhos << " " << aux->element << endl;
    else {
        cout << tracinhos << " null" << endl;
        return;
    }
    print(height+1, aux->left);
    print(height+1, aux->right);
    return;
}



void BinarySearchTreeOfInteger::add(int element) {
    root = add(root, element, NULL);
    NodoAB *aux = searchNodeRef(element, root);
    balance (aux);
    count++;
    
}

NodoAB* BinarySearchTreeOfInteger::add(NodoAB* nodo, int element, NodoAB* father){
    if (nodo == NULL) // Encontrou o lugar onde deve ser inserido
    {
        NodoAB* aux = new NodoAB(element);
        
        aux->father = father;
      
        return aux;
    }
    
    // Se elemento eh maior que o nodo atual, entao insere na sub-arvore da direita
    if (element > nodo->element) {
        nodo->right = add(nodo->right, element, nodo);

    }
    else {
        nodo->left = add(nodo->left, element, nodo);
    }
  
    return nodo;
}

int BinarySearchTreeOfInteger::height(){
    return height(root);
}

int BinarySearchTreeOfInteger::height(NodoAB *nodo){
   
    if(nodo == NULL){
        return 0;
    }

    if(nodo->left == NULL && nodo->right == NULL){
        return 1;
    }

    int heightLeft = height(nodo->left, 1);
    int heightRight = height(nodo->right, 1);
    if(heightLeft > heightRight){
        return heightLeft;
    }
    return heightRight;
}

int BinarySearchTreeOfInteger::height(NodoAB *nodo, int h){
    if(nodo == NULL){
        return h;
    }
    if (nodo->left == NULL && nodo->right == NULL){
        return h + 1;
    }

    int heightLeft = height(nodo->left, h + 1);
    int heightRight = height(nodo->right, h + 1);

    if(heightLeft >= heightRight){
        return heightLeft;
    }
    return heightRight;
}

void BinarySearchTreeOfInteger::balance(NodoAB *nodo) {
    if (nodo == NULL) {
        return;
    }
    // cout<<nodo->element<<endl;

    if (balanceValue(nodo) > 2 || balanceValue(nodo) < -2){
        cout << "Deu errado" << endl;
        return;
    }
    if (balanceValue(nodo) != 2 && balanceValue(nodo) != -2) {
        balance(nodo->father);
    }

    if (balanceValue(nodo) == -2) {
        // cout<<"Balanco = -2"<<endl;
        if (balanceValue(nodo->left) == 1) {
            rotateLeft(nodo->left);
        }
        rotateRight(nodo);
    }
    else if (balanceValue(nodo) == 2) {
        // cout<<"Balanco = 2"<<endl;
         if (balanceValue(nodo->right) == -1) {
            rotateRight(nodo->right);
            // cout << nodo->element << endl;
        }
        rotateLeft(nodo);
    }
    
}

int BinarySearchTreeOfInteger::balanceValue(NodoAB *nodo){
  
    int rightHeight = height(nodo->right);
    int leftHeight = height(nodo->left);
    return rightHeight - leftHeight;
}

BinarySearchTreeOfInteger::~BinarySearchTreeOfInteger(){
    clear();
    count = 0;
}

BinarySearchTreeOfInteger BinarySearchTreeOfInteger::clone() {
    BinarySearchTreeOfInteger clone;
    list <int> l = positionsPre();
    for (list<int>::iterator it = l.begin(); it != l.end(); it++) {
        clone.add(*it);
    }
    return clone;
}

list<int> BinarySearchTreeOfInteger::positionsPre() {
    list <int> l;
    positionsPreAux(root, l);
    return l;
}

void BinarySearchTreeOfInteger::positionsPreAux(NodoAB *nodo, list<int> &l) {
    if (nodo == NULL) {
        return;
    }
    l.push_back(nodo->element);
    positionsPreAux(nodo->left, l);
    positionsPreAux(nodo->right, l);
    return;
}




void BinarySearchTreeOfInteger::rotateRight(NodoAB *desbalanceado){
    NodoAB *esquerdo= desbalanceado->left;

    if (desbalanceado->father == nullptr) {
         if(esquerdo->right != nullptr){
            desbalanceado->left = esquerdo->right;
            desbalanceado->left->father = desbalanceado;
        }
        else{
            desbalanceado->left = nullptr;
        }
        root = esquerdo;
        root->father = nullptr;
        desbalanceado->father = esquerdo;
        root->right = desbalanceado;
    }
    else{
        if(esquerdo->right != nullptr){
            desbalanceado->left = esquerdo->right;
            desbalanceado->left->father = desbalanceado;
        }
        else{
            desbalanceado->left = nullptr;
        }
        esquerdo->father = desbalanceado->father;
        desbalanceado->father = esquerdo;
        esquerdo->right = desbalanceado;
        if (desbalanceado->element > esquerdo->father->element){
            esquerdo->father->right = esquerdo;
        }
        else{
            esquerdo->father->left = esquerdo;
        }
    }
}

void BinarySearchTreeOfInteger::rotateLeft(NodoAB *desbalanceado) {
    NodoAB *direito= desbalanceado->right;

    if (desbalanceado->father == nullptr) {
        if(direito->left != nullptr){
            desbalanceado->right = direito->left;
            desbalanceado->right->father = desbalanceado;
        }
        else{
            desbalanceado->right = nullptr;
        }
        root = direito;
        root->father = nullptr;
        desbalanceado->father = direito;
        root->left = desbalanceado;
    }
    else{
        if(direito->left != nullptr){
            desbalanceado->right = direito->left;
            desbalanceado->right->father = desbalanceado;
        }
        else{
            desbalanceado->right = nullptr;
        }
        direito->father = desbalanceado->father;
        desbalanceado->father = direito;
        direito->left = desbalanceado;
        if (desbalanceado->element > direito->father->element){
            direito->father->right = direito;
        }
        else{
            direito->father->left = direito;
        }
    }
}

NodoAB *BinarySearchTreeOfInteger::getParent(int element) {
    NodoAB *pai = searchNodeRef(element, root)->father;
    return pai;
}

void BinarySearchTreeOfInteger::clear() {
    clear(root);
    root = NULL;
}

void BinarySearchTreeOfInteger::clear(NodoAB *nodo) {
    if (nodo == NULL) {
        return;
    }
    if(nodo->left != nullptr){
        clear(nodo->left);
    }
    if(nodo->right != nullptr){
        clear(nodo->right);
    }
    delete nodo;
}

list <int> BinarySearchTreeOfInteger::positionsCentral() {
    list <int> l;
    positionsCentralAux(root, l);
    return l;
}

void BinarySearchTreeOfInteger::positionsCentralAux(NodoAB *n, list<int> &l) {
    if (n == NULL) {
        return;
    }
    positionsCentralAux(n->left, l);
    l.push_back(n->element);
    positionsCentralAux(n->right, l);
}

list <int> BinarySearchTreeOfInteger::positionsPos() {
    list <int> l;
    positionsPosAux(root, l);
    return l;
}

void BinarySearchTreeOfInteger::positionsPosAux(NodoAB *n, list<int> &l) {
    if (n == NULL) {
        return;
    }
    positionsPosAux(n->left, l);
    positionsPosAux(n->right, l);
    l.push_back(n->element);
}
