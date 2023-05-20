#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
using namespace std;

int find(vector<int>& representante, int i) {
    if (representante[i-1] != i) {
        representante[i-1] = find(representante, representante[i-1]);
    }
    return representante[i-1];
}

void unionSet(vector<int>& representante, int u, int v) {
    representante[find(representante, u)-1] = find(representante, v);
}

void kruskal(vector<tuple<int, int, float>>& listaDeArestas, int numIndices) {
    sort(listaDeArestas.begin(), listaDeArestas.end(), [](const auto& a, const auto& b) {
        return get<2>(a) < get<2>(b);
    });

    vector<int> representante(numIndices);
    for (int i = 0; i < numIndices; i++) {
        representante[i] = i + 1;
    }

    int count = 0;
    float pesoDaAGM = 0;

    for (const auto& aresta : listaDeArestas) {
        int u, v;
        float w;
        tie(u, v, w) = aresta;
        if (count == numIndices - 1) {
            break;
        }
        if (find(representante, u) != find(representante, v)) {
            pesoDaAGM += w;
            count++;
            unionSet(representante, u, v);
        }
    }

    cout << fixed;
    cout.precision(3);
    cout << pesoDaAGM << endl;
}

int main() {
    string trash;
    getline(cin, trash);
    getline(cin, trash);
    getline(cin, trash, '=');
    int numIndices;
    cin >> numIndices;
    getline(cin, trash);

    vector<tuple<int, int, float>> listaDeArestas;

    while (getline(cin, trash)) {
        if (trash.empty()) {
            break;
        }
        int u, v;
        float w;
        istringstream iss(trash);
        iss >> u >> v >> w;
        listaDeArestas.emplace_back(u, v, w);
    }

    kruskal(listaDeArestas, numIndices);

    return 0;
}
