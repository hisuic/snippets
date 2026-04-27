# HEIC → JPEG 一括変換スクリプト

`.HEIC` / `.HEIF` 画像を、**ディレクトリ構造を維持したまま `.jpg` に一括変換**するシェルスクリプトです。

* 元ファイルは削除しません
* 同じ場所に同名の `.jpg` を生成します
* 既に `.jpg` が存在する場合はスキップします

---

## 📦 必要環境

* Bash
* ImageMagick
* libheif（HEIC対応）

### インストール例

**Arch Linux**

```bash
sudo pacman -S imagemagick libheif
```

**Ubuntu**

```bash
sudo apt update
sudo apt install imagemagick libheif1 libheif-dev
```

**macOS (Homebrew)**

```bash
brew install imagemagick
```

---

## 🚀 使い方

### 実行権限を付与

```bash
chmod +x convert_heic.sh
```

---

### 実行

#### カレントディレクトリ以下を変換

```bash
./convert_heic.sh
```

#### 特定ディレクトリを指定

```bash
./convert_heic.sh "/path/to/Google Takeout"
```

---

## ⚙️ 変換設定

```bash
-quality 95
```

→ 高品質（視覚的にほぼ劣化なし）

```bash
-sampling-factor 4:4:4
```

→ 色情報を削らない（高画質）

```bash
-strip
```

→ メタデータ削除（軽量化）

---

## ⚠️ 注意点

* JPEGは非可逆圧縮のため、**理論上は劣化あり**
* ただし `quality 95` なら実用上ほぼ問題なし
