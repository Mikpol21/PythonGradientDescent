#include <bits/stdc++.h>
using namespace std;
#define mk make_pair
#define fst first
#define sz(x) x.size()
#define snd second
#define pb push_back
#define VAR(v) #v << " = " << v << " "
#define debug if(1)
#define M_PI 3.14159265358979323846
typedef complex<long double> C;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<vector<int>> Matrix;
const int maxn = (int)1e2 + 9;
const int INF = (int)1e9 + 7;
const int mod = (int)1e9 + 7;
int T, N, Q;
int order[maxn];
int ans[maxn], idx;

int ask(int a, int b, int c){
    cout<<a<<" "<<b<<" "<<c<<endl;
    int ret; cin>>ret;
    if(ret == -1)
        exit(0);
    return ret;
}

struct Node { // Navi: root -> left
    int data;
    struct Node* left;
    struct Node* right;
    Node(int val)
    {
        data = val;
        left = NULL;
        right = NULL;
    }
}; struct Node* root = NULL;

void flatten(struct Node* node){
    if(node -> left != NULL)
        flatten(node -> left);
    ans[idx++] = (*node).data;
    if(node -> right != NULL)
        flatten(node -> right);
}

void build_rec(int i, int j, struct Node **node){
    if(i > j)
        return;
    int k = (i + j) / 2;
    (*node) = new Node(ans[k]);
    build_rec(i, k - 1, &((*node) -> left));
    build_rec(k + 1, j, &((*node) -> right));

}

void rebuild(){
    idx = 0;
    flatten(root); // O(N)
    root = NULL;
    build_rec(0, idx, &root); // O(N)
}

void solve_case()
{
    random_shuffle(order, order + N);
    random_shuffle(order, order + N);
    debug{
        for(int i = 0; i < N; i++)
            ans[i] = order[i];
        idx = 0;
        build_rec(0, N, &root);
        flatten(root);
        for(int i = 0; i < N; i++)
            cout<<"("<< VAR(order[i]) << ", " << VAR(ans[i])<<") ";
        cout<<endl;
    } 
    int r = ask(order[0], order[1], order[2]);

    
}

void Adding(int val){
    int rt = (*root).data, lf = (*(root -> left)).data;
    int dir = ask(val, rt, lf);
    if(dir == rt)
        add(val, &(root -> right), root);
    else
        add(val, &(root -> left), root);
}

void add(int val, struct Node **node, struct Node *parent){
    if( (*node) == NULL){
        (*node) = new Node(val);
        return;
    }
    int v = (**node).data, par = (*parent).data;
    int dir = ask(val, v, par);
    if( parent -> left == (*node)){
        if(dir == val)
            add(val, &((*node) -> right), *node);
        else // v == dir
            add(val, &((*node) -> left), *node);
    }
    else
    {
        if(dir == val)
            add(val, &((*node) -> left), *node);
        else // v == dir
            add(val, &((*node) -> right), *node);
    }
}


int main(int argc, char* argv[])
{
    ios::sync_with_stdio(false);
    debug; else cin.tie(NULL), cout.tie(NULL);
    int case_number = 1;
    cin>>T>>N>>Q;
    for(int i = 0; i < N; i++)
        order[i] = i + 1;
    while(T--)
    {
        cout<<"Case #"<<case_number++<<": ";
        solve_case();
        int end_status;
        cin>>end_status;
        if(end_status == -1)
            break;
    }
    return 0;
}
