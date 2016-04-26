/**
 * dijkstra algorithm, shortest route
 * time complexity: O(|V| ^ 2)
 */

/**
 * dijkstra's algorithm
 * @param s [vertex s]
 * dist[i] is the shortest path from s to i
 */
void dijkstra(int s)
{
    memset(visit, false, sizeof(visit));
    visit[s] = true;

    for(int i = 0; i < n; i++)
    {
        dist[i] = graph[s][i];
    }

    int index;
    for(int i = 1; i < n; i++)
    {
        int mincost = INF;
        for(int j = 0; j < n; j++)
        {
            if(!visit[j] && dist[j] < mincost)
            {
                mincost = dist[j];
                index = j;
            }
        }

        visit[index] = true;
        for(int j = 0; j < n; j ++){
            if(!visit[j] && dist[j] > dist[index] + graph[index][j]){
                dist[j] = dist[index] + graph[index][j];
            }    
        } 
    }
}