package win.oreo.Practice;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("X : ");
        int x = sc.nextInt();
        System.out.print("Y : ");
        int y = sc.nextInt();

        List<List<Integer>> list = new ArrayList<>();

        for (int dx = 0; dx < x; dx++) {
            List<Integer> ls = new ArrayList<>();
            for (int dy = dx; dy < dx + y; dy++) {
                if (dy + 1 > y) {
                    ls.add(dy + 1 - y);
                }
                else {
                    ls.add(dy + 1);
                }
            }
            list.add(dx, ls);
        }

        for (int i = 0; i < x; i++) {
            List<Integer> ls = list.get(i);
            for (int j = 0; j < y; j++) {
                System.out.print(ls.get(j) + " ");
            }
            System.out.println("");
        }
    }
}
