import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int[] m1 = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		int[] m2 = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
		int[] m;
		
		int n = Integer.parseInt(br.readLine());
		
		int sum = 0;
		
		int cur = 4;
		
		for(int i=2019; i<=n; i++) {
			boolean yoon = check(i);
			
			
			
			if(yoon) {
				m = m2;
			}else {
				m = m1;
			}
			
			int cur_m = 1;
			
			while(true) {
				if(cur == 13) {
					sum++;
				}
				
				cur += 7;
				
				if(cur > m[cur_m]) {
					cur = cur%m[cur_m];
					
					cur_m++;
				}
				if(cur_m > 12) {
					break;
				}
				
			}
		}
		
		System.out.println(sum);
		
		


	}
	
	public static boolean check(int year) {
		if(year%400==0) {
			return true;
		}
		
		if(year%400 != 0 && year%100 == 0) {
			return false;
		}
		
		if(year%100 != 0 && year%4 == 0) {
			return true;
		}
		
		
		return false;
		
		
	}

}
