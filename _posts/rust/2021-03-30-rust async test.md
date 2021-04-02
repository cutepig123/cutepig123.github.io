代码试了几个东西

- async函数的参数能否为future？能
- future默认为不可复制，那么如何复制future呢？用FutureExt::shared
- use什么才能使用traits里面的函数？

```rust
use std::future::Future;
use futures::future::FutureExt;
use futures::executor::block_on;

async fn f1()->u8{
    2
}

async fn f2(t1: impl Future<Output=u8>, t2: impl Future<Output=u8>)->u8{
    t1.await + t2.await
}

async fn m()->u8{
    let a1 = f1().shared();
    let a2 = a1.clone();
    f2(a1, a2).await
}

async fn app(){
    let t = m().await;
    println!("Hello, world! {}", t);
}

fn main() {
    block_on(app());
    
}
```



ref

https://rust-lang.github.io/async-book/01_getting_started

