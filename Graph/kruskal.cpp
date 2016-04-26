/**
 * Kruskal's algorithm, MST(minimum spanning tree)
 * 1. create a forest F (a set of trees), where each vertex in the graph is a separate tree
 * 2. create a set S containing all the edges in the graph
 * 3. while S is nonempty and F is not yet spanning
 *      remove an edge with minimum weight from S
 *      if the removed edge connects two different trees then add it to the forest F, combining two trees into a single tree
 * 4. At the termination of the algorithm, the forest forms a minimum spanning forest of the graph. 
 *     If the graph is connected, the forest has a single component and forms a minimum spanning tree.
 * time complexity: O(|E|log|V|)
 */

const int size = 128;
int n;
int father[size];

typedef struct node
{
    int val;
    int start;
    int end;
}edge[size * size / 2];

void make_set()
{
    for (int i = 0; i < n; i++)
    {
        father[i] = i;
    }
    return;
}


/**
 * find the root of a set
 * @param  x [element of set]
 * @return   [root of set]
 */
int find_set(int x)
{
    if(x != father[x])
    {
        father[x] = find_set(father[x]);
    }
    return father[x];
}

/**
 * union two set
 * @param x [element of set one]
 * @param y [element of set two]
 */
void Union(int x, int y)
{
    x = find_set(x);    
    y = find_set(y);
    if(x == y){
        return ;    
    }
    else
    {
        father[x] = y;
    }
    return ;
}

int kruskal(int n)
{
    int sum = 0;
    make_set();
    for(int i = 0; i < n; i++)
    {
        if(find_set(edge[i].start) != find_set(edge[i].end))
        {
            Union(edge[i].start, edge[i].end);
            sum += enge[i].val;
        }
    }
    return sum;
}