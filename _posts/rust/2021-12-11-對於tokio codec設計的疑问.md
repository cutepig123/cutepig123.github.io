# 對於tokio codec設計的疑问

https://tokio.rs/tokio/tutorial/framing
https://stackoverflow.com/questions/42164981/how-to-achieve-zero-copy-in-tokio-coreiocodecdecode

Q1：文章实现了一个Buffered reads，但我想知道有无这个必要？socket内部不是已经有缓冲了吗？这样做在性能上能好多少？

Q2：缓冲写：我理解缓冲写的有效性，但对于它的设计有些担忧
decode函數輸入一個bytemut，函數需要分析是否包含一个足夠的frame。如果不夠，则应该返回ok none。
這個有幾個問題
他如何告訴上層應該讀入多少數據才能繼續decode? 如果上層不停的無效調用decode很無聊

我的想法。這個更有效的實現是。讓decode裏面可以直接從socket讀取數據

Q3：这是他的还重读的代码，我有个疑问就是如果buffer已经满了，这段代码`if 0 == self.stream.read_buf(&mut self.buffer).await?`还能读到数据吗？

Q4：还是如下代码，个人感觉代码的可读性方面不好。太多if-else

```rust
pub async fn read_frame(&mut self)
    -> Result<Option<Frame>>
{
    loop {
        // Attempt to parse a frame from the buffered data. If
        // enough data has been buffered, the frame is
        // returned.
        if let Some(frame) = self.parse_frame()? {
            return Ok(Some(frame));
        }

        // There is not enough buffered data to read a frame.
        // Attempt to read more data from the socket.
        //
        // On success, the number of bytes is returned. `0`
        // indicates "end of stream".
        if 0 == self.stream.read_buf(&mut self.buffer).await? {
            // The remote closed the connection. For this to be
            // a clean shutdown, there should be no data in the
            // read buffer. If there is, this means that the
            // peer closed the socket while sending a frame.
            if self.buffer.is_empty() {
                return Ok(None);
            } else {
                return Err("connection reset by peer".into());
            }
        }
    }
}
```



虽然有不少问题，还是学到了不少的

- 考虑到解耦，设计了很多组件和概念
- 比如缓冲写入。[`BufWriter`struct](https://docs.rs/tokio/1/tokio/io/struct.BufWriter.html)的设计很不错
- 比如stream，frame等概念
- 