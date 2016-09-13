#undef NDEBUG
#include <uchardet/uchardet.h>
#include <cassert>
#include <string.h>

int main()
{
  const char* bytes = "abc";
  size_t length = strlen(bytes);
  // Detect character code set
  uchardet_t ucd = uchardet_new();
  if (uchardet_handle_data(ucd, bytes, length) != 0) {
    assert(0);
  }

  uchardet_data_end(ucd);
  const char* charSetName = uchardet_get_charset(ucd);
  assert(strcmp(charSetName, "ASCII") == 0);
  return 0;
}
