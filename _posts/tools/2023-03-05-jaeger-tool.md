# 目標

- [ ] 默認以線程為span的父子關係
- [ ] child_of有更高優先級
- [ ] 支持通過attr名字和>+對應來匹配兩個span，進而把一個span所在的root的parent設置為另一個span
- [ ] 生成可以倒入jaegerui的json file

# 設計

- [ ] Logs: 讀入log，生成Logs
- [ ] Span: 遍歷Logs，生成Span，以及GetSpanByRow
- [ ] +>: 給定需要match的attr name，遍歷Logs，filter by attr name以及把+>放到dict裡面來加速對應關係，生成Matches
- [ ] 通過Matches修改Span的父子關係
- [ ] Export to JSON

```cpp
// Log的每一行為一個dict
struct Row
{
	map<string, string> attrs;
}

typedef vector<Row>	Logs;

// 每一個Trace為一棵樹，樹的子節點為child span，value為row
struct Span
{
	int openTagIndex;
    int closeTagIndex;
    vector<int> eventIndexes;
    vector<Span> children;
    
    const Span* parent() const;
    const Span* root() const;    
    void setParent(Span const& span)    // 修改parent
    {
        // 刪除原先的parent的指針
        // 移動到新的parent下面
    }
};
typedef Span Trace;
typedef vector<Trace> Traces;

// 每一個row的Span
Span* GetSpanByRow(rowIndex);

// +> 對應
struct Match
{
    int fromIndex;
    int toIndex;
}
typedef vecotor<Match> Matches;
```

