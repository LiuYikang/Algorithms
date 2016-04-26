/**
 * prime algorithm
 * MST(minimum spanning tree)
 * 1. Empty the spanning tree, and put a random vertex in the tree
 * 2. Get a vertex v from the set of the spanning tree, and get a vertex w form the set 
 *     out of the spanning tree, v and w has the smallest weight edge, 
 *     put w in the spanning tree set
 * 3. repeat 2, at last put all vertex in the spanning tree, it's the minimun spanning tree
 * time complexity: 
 *     adjacency list: O(|E|log|V|)
 *     adjacency matrix: O(|V|^2)
 */


/**
 * prime with adjacency matrix
 * @param  cur [start vertex]
 * @return sum [the sum of the minimum spanning tree edges]
 */
int prime(int cur)
{
    int index;
    int sum = 0;
    memset(visit, false, sizeof(visit));
    visit[cur] = true;

    for(int i = 0; i < m; i ++)
    {
        dist[i] = graph[cur][i];    
    }

    for(int i = 1; i < m; i++)
    {
        int mincost = INF;
        for (int j = 0; j < m; j+=)
        {
            if(!visit[j] && dist[j] < mincost)
            {
                mincost = dist[j];
                index = j;
            }
        }

        visit[index] = true;
        sum += mincost;

        for(int j = 0; j < m; j++)
        {
            if(!visit[j] && dist[j] > graph[index][j])
            {
                dist[j] = graph[index][j];
            }
        }
    }
    return sum;
}