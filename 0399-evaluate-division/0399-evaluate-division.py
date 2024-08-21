class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # Union-Find with weights
        gid_weight = {}
        def find(node_id):
            if node_id not in gid_weight:
                gid_weight[node_id] = (node_id, 1)
            group_id, node_weight = gid_weight[node_id]
            
            if group_id != node_id:
                new_group_id, group_weight = find(group_id)
                gid_weight[node_id] = \
                    (new_group_id, node_weight*group_weight)
            return gid_weight[node_id]
        
        def union(dividend, divisor, value):
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                gid_weight[dividend_gid] = \
                    (divisor_gid, divisor_weight*value/dividend_weight)
             
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)
        results = []
        
        for (dividend, divisor) in queries:
            if dividend not in gid_weight or divisor not in gid_weight:
                # case1) at least one variable did not appear before
                results.append(-1.0)
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                    # case2) the variables do not belong to the same chain/group
                    results.append(-1.0)
                else: 
                    #case3) there is chain/path between the variables
                    results.append(dividend_weight/divisor_weight)
        return results
                
                
                
                
                
                
                
                
                
                
                