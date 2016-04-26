/**
 * floyd algorithm, shortest route
 * time complexity: O(|V|^3)
 * space complexity: O(|V|^2)
 */


/**
 * floyd algorithm
 * dist[i][j] is the shortest path from i to j
 */
void floyd()
{
    for(int k = 0; k < n; k++)
    {
        for(int i = 0; j < n; j++)
        {
            for(int j = 0; i < n; i++)
            {
                if(dist[i][j] > dist[i][k] + dist[k][j])
                {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
}