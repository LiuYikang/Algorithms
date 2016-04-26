/**
 * The function of STL
 */

/**
 * Deque
 */
#include <deque>

const static int n = 10;

/*constructed function*/
deque<int> q1;             //empty deque
deque<int> q2(n);          //empty deque with size n
deque<int> q3(n, 0);       //deque with size n, all element is 0
deque<int> q4(q3);         //copy deque from q3
deque<int> q5(1, 10);      //deque with element of [1, 10]

q3.size();
q3.empty();
q3.max_size();
q3.at(i);                  //get the element of index i,if i > size, return out_of_range
q3[i];                     //get the element of index i, do not check size
q3.front();                //first element
q3.back();                 //last element
q3.begin();                //return a iterator, point to the first element
q3.end();                  //return a iterator, point to the last element

q3.push_back(elem);
q3.push_front(elem);
q3.pop_back();
q3.pop_front();
q3.erase(index);           //delete the element of index

q3.insert(index, elem);
q3.insert(index, n, elem);
q3.insert(index, begin, end);
q3.resize(num);
q3.resize(num, elem);
q3.clear();

/**
 * map
 */
#include <map>
#include <string>

map<int, string> ht;

ht[0] = "name";

int nFindKey = 2; //the key want find

if(ht.find(nFindKey) == enumMap.end()) {

//do not find

}

else {

//find

}

if(0 == count(key)
{
    //do not find
}
else
{
    //find
}

ht.erase(key);    //delete the (key, value)


/**
 * stack
 */
#include <stack>
stack<int> s;
s.push();
s.pop();
s.empty();
s.top();
s.size();


/**
 * queue
 */
#include <queue>
queue<int> q;
q.back();
q.empty();
q.front();
q.pop();
q.push();
q.size();


/**
 * set
 * The C++ Set is an associative container that contains a sorted set of unique objects
 */
#include <set>

typedef struct ss{

};

struct cmp{
    bool operator()(const int &a, const int &b)const)
    {

    }
};

set<ss> base;

base.begin();
base.end();
base.clear();
base.empty();
base.erase(ele);
base.count(ele);
base.find(ele);
base.size();

/**
 * vector
 */
#include <vector>

vector <Elem> c;
vector <Elem> c1(c2);
vector <Elem> c(n);
vector <Elem> c(n, elem);
vector <Elem> c(beg,end);
c.~ vector <Elem>();

c.clear();
c.empty();
c.begin();
c.end();
c.size();
c.push_back(ele);
c.pop_back();
c.front();
c.back();