Comment Rules
-------------

comment_001
###########

This rule aligns comments above library use statements with the use statement.

**Violation**

.. code-block:: vhdl

    library ieee;
    -- Use standard logic library
      use ieee.std_logic_1164.all;

**Fix**

.. code-block:: vhdl

    library ieee;
      -- Use standard logic library
      use ieee.std_logic_1164.all;

comment_003
###########

This rule checks the alignment of in line comments between the process begin and end process lines.

**Violation**

.. code-block:: vhdl

   PROC_1: process () is
   begin

     a <= '1';   -- Assert
     b <= '0';       -- Deassert
     c <= '1'; -- Enable

   end process PROC_1;

**Fix**

.. code-block:: vhdl

   PROC_1: process () is
   begin

     a <= '1';       -- Assert
     b <= '0';       -- Deassert
     c <= '1';       -- Enable

   end process PROC_1;

comment_004
###########

This rule checks for at least a single space before inline comments.

**Violation**

.. code-block:: vhdl

   wr_en <= '1';--Write data
   rd_en <= '1';   -- Read data

**Fix**

.. code-block:: vhdl

   wr_en <= '1'; --Write data
   rd_en <= '1';   -- Read data

comment_005
###########

This rule aligns consecutive comment only lines above a **when** keyword in a case statement with the **when** keyword.

**Violation**

.. code-block:: vhdl

       -- comment 1
 -- comment 2
    -- comment 3
   when wr_en =>
     rd_en <= '0';

**Fix**

.. code-block:: vhdl

   -- comment 1
   -- comment 2
   -- comment 3
   when wr_en =>
     rd_en <= '0';

comment_006
###########

This rule aligns in line comments between the end of the process sensitivity list and the process **begin** keyword.

**Violation**

.. code-block:: vhdl

   PROC_1 : process () is

      variable counter : integer range 0 to 31;     -- Counts the number of frames received
      variable width   : natural range 0 to 255; -- Keeps track of the data word size

      variable size    : natural range 0 to 7; -- Keeps track of the frame size

   begin

**Fix**

.. code-block:: vhdl

   PROC_1 : process () is

      variable counter : integer range 0 to 31;     -- Counts the number of frames received
      variable width   : natural range 0 to 255;    -- Keeps track of the data word size

      variable size    : natural range 0 to 7;      -- Keeps track of the frame size

   begin

comment_008
###########

This rule aligns consecutive comment only lines above the **elsif** keyword in if statements.
These comments are used to describe what the elsif code is going to do.

**Violation**

.. code-block:: vhdl

       -- comment 1
 -- comment 2
    -- comment 3
   elsif (a = '1')
     rd_en <= '0';

**Fix**

.. code-block:: vhdl

   -- comment 1
   -- comment 2
   -- comment 3
   elsif (a = '1')
     rd_en <= '0';

comment_009
###########

This rule aligns consecutive comment only lines above the **else** keyword in if statements.
These comments are used to describe what the elsif code is going to do.

**Violation**

.. code-block:: vhdl

       -- comment 1
 -- comment 2
    -- comment 3
   else
     rd_en <= '0';

**Fix**

.. code-block:: vhdl

   -- comment 1
   -- comment 2
   -- comment 3
   else
     rd_en <= '0';

comment_010
###########

This rule checks the indent lines starting with comments.

**Violation**

.. code-block:: vhdl

       -- Libraries
   libary ieee;

    -- Define architecture
   architecture RTL of FIFO is

   -- Define signals
     signal wr_en : std_logic;
     signal rd_en : std_Logic;

   begin

**Fix**

.. code-block:: vhdl

   -- Libraries
   libary ieee;

   -- Define architecture
   architecture RTL of FIFO is

     -- Define signals
     signal wr_en : std_logic;
     signal rd_en : std_Logic;

   begin


