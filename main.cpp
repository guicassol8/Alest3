#include <iostream>
#include "BinarySearchTreeOfInteger.h"

using namespace std;

int main (){
	BinarySearchTreeOfInteger tree;
	tree.add(120);
	tree.add(110);
	tree.add(150);
	tree.add(80);
	tree.add(130);
	tree.add(200);
	tree.add(100);
	// tree.add(100);
	// tree.add(42);
	// tree.add(150);
	// tree.add(15);
	// tree.add(160);
	// tree.add(88);
	// tree.add(120);
	// tree.add(94);
	// tree.add(130);
	// tree.add(67);
	// tree.add(90);
	tree.print();
	cout << tree.getParent(130)->element << endl;
	list <int> lista = tree.positionsPos();
	for (list<int>::iterator it = lista.begin(); it != lista.end(); it++){
		cout << *it << " ";
	}
	return 0;
}