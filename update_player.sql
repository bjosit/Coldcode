CREATE PROCEDURE `update_balance`(
	IN `player` VARCHAR(50),
	IN `tbalance` FLOAT
)
LANGUAGE SQL
NOT DETERMINISTIC
CONTAINS SQL
SQL SECURITY DEFINER
COMMENT ''
BEGIN
INSERT INTO iglo (player_id, balance)
VALUES (@player, @tbalance)
ON DUPLICATE KEY UPDATE
   balance = (balance+@tbalance);
END
