class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        unordered_map<int, int>degree;
        
        for (vector<int> edge:edges) {
            degree[edge[0]]++;
            degree[edge[1]]++;
        }
        
        for (pair<int, int>nodes:degree) {
            int node = nodes.first;
            int nodeDegree = nodes.second;
            
            if(nodeDegree == edges.size()) {
                return node;
            }
        }
        
        return -1;

    }
};

// Greedy ver. 

// class Solution {
// public:
//     int findCenter(vector<vector<int>>& edges) {
//         vector<int> firstEdge = edges[0];
//         vector<int> secondEdge = edges[1];

//         return (firstEdge[0] == secondEdge[0] || firstEdge[0] == secondEdge[1])
//                    ? firstEdge[0]
//                    : firstEdge[1];
//     }
// };