/**
 * BFS
 * time complexity:
 *     1. adjacency list: O(|V|+|E|)
 *     2. adjacency matrix: O(|V|^2)
 * space complexity: use a queue, O(|V|)
 */

#include <isotream>
#include <list>

using namespace std;

/* adjacency list with directed graph */
class graph
{
    int V;
    list<int> *adj;
    void BFSUtil(int v, bool visited[]);

public:
    graph(int v);
    void addEdge(int v, int w);
    void BFS(int v);
};

/*
constructor
 */
graph::graph(int v)
{
    this->V = v;
    adj = new list<int>[V];
}

/**
 * add an edge and construct a adjacency list
 */
void graph::addEdge(int v, int w)
{
    adj[v].push_back(w);
    //if graph is an undirected graph
    //adj[w].push_back(v);
}

/**
 * BFS from vertex v
 */
void graph::BFSUtil(int v, bool visited[])
{
    list<int> queue;

    queue.push_back(v);

    list<int>::iterator i;

    while(!queue.empty())
    {
        v = queue.front();
        cout << v << " ";
        visited[v] = true;
        queue.pop_front();

        for(i = adj[v].begin(); i != adj[v].end(); i++)
        {
            if(!visited[*i])
            {
                queue.push_back(*i);
            }
        }
    }
}

/**
 * BFS
 */
void graph::BFS(int v)
{
    bool *visited = new bool[V];
    for(int i = 0; i < v; i++)
    {
        visited[i] = false;
    }
    for(int i=0; i<V; ++i)
    {
        if(!visited[i])
            BFSUtil(i, visited);
    }
}


int main()
{
    Graph g(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);

    cout << "Following is BFS Traversal (starting from vertex 2) \n";
    g.BFS(2);
    cout << endl;

    return 0;
}