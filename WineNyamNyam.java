package coala;
import java.util.Scanner;


public class WineNyamNyam {
	
		public static void main(String[] args) {
			
			System.out.println("������ �� ���� �ֳĸ�~");
			Scanner sc = new Scanner(System.in);
	 
			int n = sc.nextInt();
			
	 
			int[] a = new int[n + 1];
			int[] biggest = new int[n + 1];
	 
			for (int i = 1; i <= n; i++) {
				a[i] = sc.nextInt();
			}
	 
			biggest[1] = a[1]; 
			
			if (n > 1) 
				biggest[2] = a[1] + a[2];//n=1,2�� ���
			
			for (int i = 3; i <= n; i++) {//n>=3����!
				
				biggest[i] = Math.max(biggest[i - 1], Math.max(biggest[i - 2] + a[i], biggest[i - 3] + a[i - 1] + a[i]));
	 
			}
			System.out.println("�ִ�� ���� �� �ִ� ���� "+biggest[n]);
		}
	 
	}


