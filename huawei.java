import java.util.*;

public class Main{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);
		while(in.hasNext())
		{
			HashMap<Integer, HashSet<Integer>> m = new HashMap<Integer, HashSet<Integer>>();
			String input;
			int send = 0;
			input = in.nextLine();
			if(input.equals("Sender"))send = Integer.parseInt(in.nextLine());
			input = in.nextLine();
			if(input.equals("Relationship"))
			{
				input = in.nextLine();
				while(!input.equals("End"))
				{
					String[] tmp = input.split(",");
					int a = Integer.parseInt(tmp[0]);
					int b = Integer.parseInt(tmp[1]);
					if(!m.containsKey(a))m.put(a, new HashSet<Integer>());
					m.get(a).add(b);
					if(!m.containsKey(b))m.put(b, new HashSet<Integer>());
					m.get(b).add(a);
					input = in.nextLine();
				}
			}
			
			HashMap<Integer, Integer> time = new HashMap<Integer, Integer>();
			time.put(send, 0);
			Queue<Integer> q = new LinkedList<Integer>();
			q.add(send);
			
			int total = -1;
			while(!q.isEmpty())
			{
				Integer node = q.poll();
				if(!m.containsKey(node))continue;
				HashSet tmpSet = m.get(node);
				int count = time.get(node);
				
				Iterator<Integer> it = tmpSet.iterator();
				boolean flag = false;
				while(it.hasNext())
				{
					Integer tmpNode = it.next();
					if(!time.containsKey(tmpNode))
					{
						time.put(tmpNode, count+1);
						flag = true;
						q.add(tmpNode);
					}
				}
				if(flag)total++;
			}
			System.out.println(total);
		}
	}
}
