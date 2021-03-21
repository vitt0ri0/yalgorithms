import java.io.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicReference;

import static java.lang.Integer.parseInt;

public class Task {

    public static void main(String[] args) throws IOException {
        try (BufferedReader br = new BufferedReader(new FileReader("input.txt"), 15000);
             BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out), 15000)) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int totalNodes = parseInt(st.nextToken());
            int totalEdges = parseInt(st.nextToken());

            Graph graph = new Graph(totalNodes);
            for (int j = 0; j < totalEdges; j++) {
                st = new StringTokenizer(br.readLine());
                int k = parseInt(st.nextToken());
                int l = parseInt(st.nextToken());
                graph.addEdge(k, l);
                graph.addEdge(l, k);
            }
            Map<Integer, List<Integer>> connectivityComponentEdges = graph.dfsFindConnectivityComponents();

            prettyPrintResult(bw, connectivityComponentEdges);
            bw.flush();
        }
    }

    public static class Graph {
        private static final int COLOR_DEFAULT_VALUE = -1;
        int[] colors;
        List<Integer>[] edges;
        int connectivityComponents;

        public Graph(int totalNodes) {
            edges = new List[totalNodes];
            colors = new int[totalNodes];
            Arrays.fill(colors, COLOR_DEFAULT_VALUE);
            connectivityComponents = 0;
        }

        public void addEdge(int vertex1, int vertex2) {
            if (vertex1 != vertex2) {
                if (edges[vertex1 - 1] == null) {
                    edges[vertex1 - 1] = new LinkedList<>();
                }
                edges[vertex1 - 1].add(vertex2 - 1);
            }
        }

        public Map<Integer, List<Integer>> dfsFindConnectivityComponents() throws IOException {
            for (int i = 0; i < colors.length; i++) {
                if (colors[i] == COLOR_DEFAULT_VALUE) {
                    connectivityComponents++;
                    innerPrintDfs(i);
                }
            }

            Map<Integer, List<Integer>> connectivityComponentEdges = new LinkedHashMap<>(connectivityComponents, 1);
            for (int i = 0; i < colors.length; i++) {
                List<Integer> nodes = connectivityComponentEdges.get(colors[i] - 1);
                if (nodes == null) {
                    nodes = new ArrayList<>();
                    connectivityComponentEdges.put(colors[i] - 1, nodes);
                }
                nodes.add(i);
            }

            return connectivityComponentEdges;
        }

        private void innerPrintDfs(int node) {
            colors[node] = connectivityComponents;
            List<Integer> edgeNodes = edges[node];
            if (edgeNodes != null) {
                edgeNodes.sort(Integer::compareTo);
                for (Integer edgeNode: edgeNodes) {
                    if (colors[edgeNode] == COLOR_DEFAULT_VALUE) {
                        colors[edgeNode] = connectivityComponents;
                        innerPrintDfs(edgeNode);
                    }
                }
            }
        }
    }

    private static void prettyPrintResult(BufferedWriter bw, Map<Integer, List<Integer>> connectivityComponentEdges) throws IOException {
        bw.append(connectivityComponentEdges.size() + "\n");
        String rowDelim = "";
        for (Map.Entry<Integer, List<Integer>> e : connectivityComponentEdges.entrySet()) {
            bw.append(rowDelim);
            String wordDelim = "";
            for (Integer node : e.getValue()) {
                bw.append(wordDelim + (node + 1));
                wordDelim = " ";
            }
            rowDelim = "\n";
        }
    }
}

