import java.io.*;
import java.util.*;

public class Main {
    static int[] deltas = {-1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        Deque<Integer> queue = new LinkedList<>();
        queue.offer(N);
        HashMap<Integer, Integer> dist = new HashMap<>();
        dist.put(N, 0);
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            if (cur == K) break;
            int nxt = cur * 2;
            if (nxt >= 0 && cur <= K && !dist.containsKey(nxt) ) {
                queue.offerFirst(nxt);
                dist.put(nxt, dist.get(cur));
            }
            for (int delta : deltas) {
                nxt = cur + delta;
                if (nxt >= 0 && !dist.containsKey(nxt)) {
                    queue.offer(nxt);
                    dist.put(nxt, dist.get(cur) + 1);
                }
            }
        }
        bw.write(String.valueOf(dist.get(K)));
        bw.flush();
    }
}