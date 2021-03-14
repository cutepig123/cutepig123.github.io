---
categories: rust
---
```rust
use std::sync::Mutex;
use std::sync::Arc;
use std::{thread};

fn main() {
    // Typical multi thread patterns
    let data = Arc::new(Mutex::new(vec![1u32, 2, 3]));
    let mut handles = vec![];

    for i in 0..3 {
        let data = data.clone();
        let handle = thread::spawn(move || {
            let mut datax = data.lock().unwrap();
            datax[i] += 1;
        });
        handles.push(handle);
    }

    for handle in handles {
        handle.join().unwrap();
    }
}
```